#!/usr/bin/env python3
"""
Crop Tool — Claude API Test Suite

Runs each test image through two passes:
  - WITHOUT crop tool: Claude analyzes the full image directly
  - WITH crop tool: Claude crops, enhances, and analyzes regions

Supports both stock test images and your own images via fixtures/.

Requires: ANTHROPIC_API_KEY environment variable set
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from crop_tool import ask_with_crop_tool, pil_to_base64
from anthropic import Anthropic
from PIL import Image


# Stock test cases — included in test_images/
STOCK_TESTS = [
    {
        "filename": "bar_chart.png",
        "description": "Bar Chart — Quarterly Sales",
        "question": "What are the approximate sales values for each quarter? List them.",
    },
    {
        "filename": "pie_chart.png",
        "description": "Pie Chart — Market Share",
        "question": "What are the market share percentages for each product? Identify the largest segment.",
    },
    {
        "filename": "table_document.png",
        "description": "Table Document — Sales Report",
        "question": "What are the product names and their revenue values? List them clearly.",
    },
    {
        "filename": "technical_diagram.png",
        "description": "Technical Diagram — System Architecture",
        "question": "What are the main components in this system and how are they connected?",
    },
    {
        "filename": "challenging_chart.png",
        "description": "Challenging Chart — Revenue Analysis (Small Text)",
        "question": "What are the exact revenue values for Q1, Q2, Q3, and Q4? Read the legend carefully. And read the text at the bottom box of Q3.",
        "expected_values": ["125", "250", "187.5", "312"],
    },
]


def run_comparison(client, image, description, question, expected_values=None):
    """
    Run a single image through with/without crop tool comparison.

    Returns a result dict with both answers and optional accuracy scores.
    """
    print(f"\n{'=' * 70}")
    print(f"{description}")
    print(f"{'=' * 70}")
    print(f"Question: {question}\n")

    # --- WITHOUT crop tool ---
    print("[ WITHOUT Crop Tool ]")
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": question},
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": pil_to_base64(image),
                    },
                },
            ],
        }
    ]
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            messages=messages,
        )
        answer_without = response.content[0].text
        print(f"{answer_without}\n")
    except Exception as e:
        answer_without = f"ERROR: {e}"
        print(f"❌ {answer_without}\n")

    # --- WITH crop tool ---
    print("[ WITH Crop Tool ]")
    try:
        answer_with = ask_with_crop_tool(
            image=image,
            question=question,
            model="claude-haiku-4-5-20251001",
            client=client,
        )
        print(f"{answer_with}\n")
    except Exception as e:
        answer_with = f"ERROR: {e}"
        print(f"❌ {answer_with}\n")

    # --- Accuracy check (if expected values provided) ---
    if expected_values:
        without_found = sum(1 for val in expected_values if val in answer_without)
        with_found = sum(1 for val in expected_values if val in answer_with)
        total = len(expected_values)
        print(f"Expected values: {expected_values}")
        print(f"  WITHOUT crop tool: {without_found}/{total} correct")
        print(f"  WITH crop tool:    {with_found}/{total} correct")
        if with_found > without_found:
            print(f"  ✅ Crop tool improved accuracy by +{with_found - without_found}\n")
        elif with_found == without_found:
            print(f"  ⚠️  Same accuracy with and without crop tool\n")
        else:
            print(f"  ⚠️  Both methods struggled with this image\n")

    return {
        "description": description,
        "answer_without": answer_without,
        "answer_with": answer_with,
        "expected_values": expected_values,
    }


def main():
    print("\n🧪 CROP TOOL SKILL — CLAUDE API TEST SUITE\n")

    client = Anthropic()
    test_images_dir = Path(__file__).parent / "test_images"
    fixtures_dir = Path(__file__).parent / "fixtures"

    results = []

    # --- Stock test images ---
    print(f"{'=' * 70}")
    print("STOCK TEST IMAGES")
    print(f"{'=' * 70}")

    for test in STOCK_TESTS:
        image_path = test_images_dir / test["filename"]
        if not image_path.exists():
            print(f"\n⚠️  Skipping {test['filename']} — not found in test_images/")
            continue
        image = Image.open(image_path)
        result = run_comparison(
            client,
            image,
            test["description"],
            test["question"],
            test.get("expected_values"),
        )
        results.append(result)

    # --- Fixture images (user-provided) ---
    fixture_images = sorted(
        [f for f in fixtures_dir.glob("*")
         if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
         and f.name != ".gitkeep"]
    )

    if fixture_images:
        print(f"\n{'=' * 70}")
        print("YOUR IMAGES (fixtures/)")
        print(f"{'=' * 70}")
        for image_path in fixture_images:
            image = Image.open(image_path)
            result = run_comparison(
                client,
                image,
                f"Fixture: {image_path.name}",
                "Analyze this image in detail. Read any text, values, or labels you can find.",
            )
            results.append(result)
    else:
        print(f"\n💡 Tip: Add your own images to fixtures/ to test them too.\n")

    # --- Summary ---
    print(f"\n{'=' * 70}")
    print(f"TEST COMPLETE — {len(results)} image(s) analyzed")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    sys.exit(main())
