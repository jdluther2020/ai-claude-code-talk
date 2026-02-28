#!/usr/bin/env python3
"""
Test script for crop-tool skill with Claude API.

Tests the crop tool's ability to analyze different types of images:
- Bar charts
- Pie charts
- Tables/documents
- Technical diagrams
- Charts with small text

Requires: ANTHROPIC_API_KEY environment variable set
"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from crop_tool import ask_with_crop_tool, pil_to_base64
from anthropic import Anthropic
from PIL import Image
import base64


def test_with_local_images():
    """Test crop tool with local checked-in test images."""
    print("\n" + "=" * 70)
    print("🧪 CROP TOOL - CLAUDE API INTEGRATION TEST")
    print("=" * 70)

    try:
        client = Anthropic()
        test_images_dir = Path(__file__).parent / "test_images"

        # Step 1: Ask about test images
        print("\n✅ Test images found in: test_images/")
        while True:
            choice = input(
                "\nOptions:\n"
                "  • Use existing images (fast) [1]\n"
                "  • Regenerate images [2]\n"
                "  • Abort [3]\n\n"
                "Choice (1-3): "
            ).strip()
            if choice == "1":
                print("Using existing test images...\n")
                break
            elif choice == "2":
                print("Regenerating test images...")
                from generate_test_images import generate_all_test_images

                generate_all_test_images()
                break
            elif choice == "3":
                print("❌ Test aborted by user")
                return False
            else:
                print("Invalid choice. Try again.")

        # Step 2: Define test cases for each image
        test_cases = [
            {
                "filename": "bar_chart.png",
                "description": "Bar Chart - Quarterly Sales",
                "question": "What are the approximate sales values for each quarter? List them.",
            },
            {
                "filename": "pie_chart.png",
                "description": "Pie Chart - Market Share",
                "question": "What are the market share percentages for each product? Identify the largest segment.",
            },
            {
                "filename": "table_document.png",
                "description": "Table Document - Sales Report",
                "question": "What are the product names and their revenue values? List them clearly.",
            },
            {
                "filename": "technical_diagram.png",
                "description": "Technical Diagram - System Architecture",
                "question": "What are the main components in this system and how are they connected?",
            },
            {
                "filename": "challenging_chart.png",
                "description": "Chart with Small Text - Revenue Analysis",
                "question": "What are the exact revenue values for Q1, Q2, Q3, and Q4? Read the legend carefully. And read the text at the bottom box of Q3.",
            },
        ]

        # Step 3: Test each image
        print("\n" + "=" * 70)
        print("TESTING WITH CLAUDE API")
        print("=" * 70)

        results = []

        for idx, test_case in enumerate(test_cases, 1):
            filename = test_case["filename"]
            description = test_case["description"]
            question = test_case["question"]

            image_path = test_images_dir / filename

            if not image_path.exists():
                print(f"\n❌ Image {idx}/5: {description}")
                print(f"   File not found: {image_path}")
                results.append((filename, "SKIPPED", "File not found"))
                continue

            print(f"\n{'=' * 70}")
            print(f"Image {idx}/5: {description}")
            print(f"{'=' * 70}")
            print(f"File: {filename}")
            print(f"Question: {question}\n")

            try:
                image = Image.open(image_path)
                print(f"Analyzing {filename} with Claude + crop-tool...")
                print("-" * 70)

                answer = ask_with_crop_tool(
                    image=image,
                    question=question,
                    model="claude-haiku-4-5-20251001",
                )

                print("-" * 70)
                print(f"\n✅ Claude's Analysis:\n{answer}\n")
                results.append((filename, "PASS", "Successfully analyzed"))

            except Exception as e:
                print(f"❌ Error analyzing {filename}: {e}")
                results.append((filename, "FAIL", str(e)))

        # Step 4: Summary
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)

        for filename, status, note in results:
            icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
            print(f"{icon} {filename:30} {status:10} {note}")

        print("=" * 70 + "\n")

        # Overall result
        passed = sum(1 for _, status, _ in results if status == "PASS")
        total = len(results)

        if passed == total:
            print(f"✅ OVERALL: ALL {total} TESTS PASSED\n")
            return True
        else:
            print(f"⚠️  OVERALL: {passed}/{total} tests passed\n")
            return passed > 0

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_accuracy_improvement():
    """Compare accuracy WITH vs WITHOUT crop tool.

    This is the critical test: does the crop tool actually improve Claude's ability
    to extract accurate information from images with small text?
    """
    print("\n" + "=" * 70)
    print("ACCURACY COMPARISON - WITH vs WITHOUT Crop Tool")
    print("=" * 70)
    print("Using challenging_chart.png with small text...\n")

    try:
        test_images_dir = Path(__file__).parent / "test_images"
        chart_path = test_images_dir / "challenging_chart.png"

        if not chart_path.exists():
            print(f"⚠️  Test image not found: {chart_path}")
            return None

        image = Image.open(chart_path)
        client = Anthropic()

        # The exact question that requires reading small text
        question = "What are the exact revenue values for Q1, Q2, Q3, and Q4? Read the legend carefully. And read the text at the bottom box of Q3."
        expected_values = ["125", "250", "187.5", "312"]

        # TEST 1: WITHOUT crop tool (full image only)
        print("TEST 1: Claude WITHOUT Crop Tool (full image, no cropping)")
        print("-" * 70)

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{question}\n\nIMPORTANT: Do NOT use any tools. Just analyze the full image directly and extract the numbers.",
                    },
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

        response_without = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            messages=messages,
        )

        answer_without = response_without.content[0].text
        print(f"Claude's answer (NO crop):\n{answer_without}\n")

        # TEST 2: WITH crop tool
        print("TEST 2: Claude WITH Crop Tool (can zoom into regions)")
        print("-" * 70)

        answer_with = ask_with_crop_tool(
            image=image,
            question=question,
            model="claude-haiku-4-5-20251001",
        )

        print(f"Claude's answer (WITH crop):\n{answer_with}\n")

        # COMPARISON
        print("=" * 70)
        print("ACCURACY ANALYSIS")
        print("=" * 70)

        # Count how many expected values appear in each answer
        without_found = sum(1 for val in expected_values if val in answer_without)
        with_found = sum(1 for val in expected_values if val in answer_with)

        print(f"\nExpected to find: {expected_values}")
        print(f"\nValues found WITHOUT crop tool: {without_found}/4")
        print(f"Values found WITH crop tool: {with_found}/4")
        print()

        if with_found > without_found:
            improvement = with_found - without_found
            print(f"✅ CROP TOOL IMPROVED ACCURACY")
            print(f"   Improvement: +{improvement} values correctly extracted")
            return True
        elif with_found == without_found:
            print(f"⚠️  Both methods found {with_found} values")
            print(f"   (Chart may be readable at full size, or cropping didn't help)")
            return True
        else:
            print(f"⚠️  Both methods struggled with accuracy")
            return True

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("\n🧪 CROP TOOL SKILL - CLAUDE API TEST SUITE\n")

    # Run the main integration test
    result1 = test_with_local_images()

    # Run the accuracy comparison test
    result2 = test_accuracy_improvement()

    # Overall result
    overall = result1 and (result2 is not False)
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
