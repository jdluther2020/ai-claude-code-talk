#!/usr/bin/env python3
"""
Crop Tool — Amazon Bedrock Test Suite (boto3)

Mirrors test_crop_tool.py but uses Amazon Bedrock via the boto3
converse API instead of the Anthropic SDK.

Runs each test image through two passes:
  - WITHOUT crop tool: Claude on Bedrock analyzes the full image directly
  - WITH crop tool: Claude crops, enhances, and analyzes regions

Requires:
  - AWS credentials configured (aws configure, env vars, or IAM role)
  - Bedrock model access enabled in your AWS account
  - boto3 installed: pip install boto3

Run with: python3 test_crop_bedrock.py
"""

import sys
import os
import base64
from io import BytesIO
from pathlib import Path

import boto3
from PIL import Image

# Add grandparent directory to path (skills/crop-tool/)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from crop_tool import handle_crop, get_pil_image, CROP_TOOL

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# Default model — override with CLAUDE_MODEL env var
# Cross-region inference profile IDs use the "us." prefix.
DEFAULT_MODEL = os.environ.get("CLAUDE_MODEL", "us.anthropic.claude-haiku-4-5-20251001-v1:0")

# ---------------------------------------------------------------------------
# Stock test cases — same images as test_crop_tool.py
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Bedrock tool config — translates CROP_TOOL (Anthropic format) to Bedrock format
BEDROCK_TOOL_CONFIG = {
    "tools": [
        {
            "toolSpec": {
                "name": CROP_TOOL["name"],
                "description": CROP_TOOL["description"],
                "inputSchema": {
                    "json": CROP_TOOL["input_schema"],
                },
            }
        }
    ]
}


def pil_to_bytes(image: Image.Image) -> bytes:
    """Convert PIL Image to raw PNG bytes for the Bedrock converse API."""
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


def image_block(image: Image.Image) -> dict:
    """Build a Bedrock converse image content block from a PIL Image."""
    return {
        "image": {
            "format": "png",
            "source": {"bytes": pil_to_bytes(image)},
        }
    }


def crop_result_to_bedrock(result: list) -> list:
    """
    Convert handle_crop() output (Anthropic format) to Bedrock converse
    toolResult content blocks.
    """
    bedrock_content = []
    for block in result:
        if block["type"] == "text":
            bedrock_content.append({"text": block["text"]})
        elif block["type"] == "image":
            raw_bytes = base64.standard_b64decode(block["source"]["data"])
            bedrock_content.append({
                "image": {
                    "format": "png",
                    "source": {"bytes": raw_bytes},
                }
            })
    return bedrock_content


# ---------------------------------------------------------------------------
# Core: ask_with_crop_tool via Bedrock converse
# ---------------------------------------------------------------------------

def ask_with_crop_tool_bedrock(
    image: Image.Image,
    question: str,
    model: str = DEFAULT_MODEL,
    client=None,
    system_prompt: str = None,
    max_iterations: int = 10,
) -> str:
    """
    Ask Claude (on Bedrock) a question about an image, with crop tool available.

    Uses the boto3 bedrock-runtime converse API. Mirrors the behaviour of
    ask_with_crop_tool() in crop_tool.py.

    Args:
        image: PIL Image to analyze
        question: Question to ask Claude
        model: Bedrock model ID
        client: boto3 bedrock-runtime client (created if not provided)
        system_prompt: Optional system prompt
        max_iterations: Maximum agentic loop iterations

    Returns:
        Claude's final answer as string
    """
    if client is None:
        client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

    if system_prompt is None:
        system_prompt = (
            "You are a helpful assistant analyzing images. "
            "Use the crop_image tool to examine specific regions when you need detail. "
            "Provide clear, accurate analysis based on what you observe."
        )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "text": (
                        f"Please analyze this image and answer the following question:\n\n"
                        f"{question}\n\n"
                        "Use the crop_image tool to examine specific regions if you need "
                        "to see details more clearly."
                    )
                },
                image_block(image),
            ],
        }
    ]

    iteration = 0
    crops_used = 0
    print(f"\n[BEDROCK] Starting analysis with crop tool (model: {model})...")

    while iteration < max_iterations:
        iteration += 1

        response = client.converse(
            modelId=model,
            system=[{"text": system_prompt}],
            messages=messages,
            toolConfig=BEDROCK_TOOL_CONFIG,
        )

        stop_reason = response["stopReason"]
        content = response["output"]["message"]["content"]

        # Done — no more tool calls
        if stop_reason != "tool_use":
            print(f"[BEDROCK] Analysis complete. Total crops used: {crops_used}")
            for block in content:
                if "text" in block:
                    return block["text"]
            return "Analysis complete"

        # Append assistant turn
        messages.append({"role": "assistant", "content": content})

        # Execute tool calls and collect results
        tool_results = []
        for block in content:
            if "toolUse" in block:
                crops_used += 1
                tool_use = block["toolUse"]
                result = handle_crop(image, **tool_use["input"])
                tool_results.append({
                    "toolResult": {
                        "toolUseId": tool_use["toolUseId"],
                        "content": crop_result_to_bedrock(result),
                    }
                })

        messages.append({"role": "user", "content": tool_results})

    return "Analysis reached maximum iterations limit"


# ---------------------------------------------------------------------------
# Comparison runner — mirrors run_comparison() in test_crop_tool.py
# ---------------------------------------------------------------------------

def run_comparison(client, image: Image.Image, description: str, question: str,
                   model: str = DEFAULT_MODEL, expected_values=None) -> dict:
    """
    Run a single image through with/without crop tool comparison on Bedrock.
    """
    print(f"\n{'=' * 70}")
    print(f"{description}")
    print(f"{'=' * 70}")
    print(f"Question: {question}\n")

    # --- WITHOUT crop tool ---
    print("[ WITHOUT Crop Tool ]")
    try:
        response = client.converse(
            modelId=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"text": question},
                        image_block(image),
                    ],
                }
            ],
        )
        answer_without = response["output"]["message"]["content"][0]["text"]
        print(f"{answer_without}\n")
    except Exception as e:
        answer_without = f"ERROR: {e}"
        print(f"❌ {answer_without}\n")

    # --- WITH crop tool ---
    print("[ WITH Crop Tool ]")
    try:
        answer_with = ask_with_crop_tool_bedrock(
            image=image,
            question=question,
            model=model,
            client=client,
        )
        print(f"{answer_with}\n")
    except Exception as e:
        answer_with = f"ERROR: {e}"
        print(f"❌ {answer_with}\n")

    # --- Accuracy check ---
    if expected_values:
        without_found = sum(1 for v in expected_values if v in answer_without)
        with_found = sum(1 for v in expected_values if v in answer_with)
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("\n🧪 CROP TOOL SKILL — AMAZON BEDROCK TEST SUITE (boto3)\n")
    print(f"  Region : {AWS_REGION}")
    print(f"  Model  : {DEFAULT_MODEL}\n")

    client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

    test_images_dir = Path(__file__).parent.parent / "test_images"
    fixtures_dir = Path(__file__).parent.parent / "fixtures"

    results = []

    # --- Stock test images ---
    print(f"{'=' * 70}")
    print("STOCK TEST IMAGES")
    print(f"{'=' * 70}")

    for test in STOCK_TESTS:
        image_path = test_images_dir / test["filename"]
        if not image_path.exists():
            print(f"\n⚠️  Skipping {test['filename']} — not found in test_images/")
            print(f"   Run tests/generate_test_images.py first to create them.")
            continue
        image = Image.open(image_path)
        result = run_comparison(
            client,
            image,
            test["description"],
            test["question"],
            expected_values=test.get("expected_values"),
        )
        results.append(result)

    # --- Fixture images (user-provided) ---
    fixture_images = sorted(
        [f for f in fixtures_dir.glob("*")
         if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
         and f.name != ".gitkeep"]
    ) if fixtures_dir.exists() else []

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
        print(f"\n💡 Tip: Add your own images to tests/fixtures/ to test them too.\n")

    # --- Summary ---
    print(f"\n{'=' * 70}")
    print(f"TEST COMPLETE — {len(results)} image(s) analyzed via Bedrock")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    sys.exit(main())
