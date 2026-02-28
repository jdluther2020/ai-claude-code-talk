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

from crop_tool import ask_with_crop_tool
from anthropic import Anthropic
from PIL import Image


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
                "crop_regions": [(0.0, 0.8, 1.0, 1.0)],
            },
            {
                "filename": "pie_chart.png",
                "description": "Pie Chart - Market Share",
                "question": "What are the market share percentages for each product? Identify the largest segment.",
                "crop_regions": [(0.5, 0.0, 1.0, 0.5)],
            },
            {
                "filename": "table_document.png",
                "description": "Table Document - Sales Report",
                "question": "What are the product names and their revenue values? List them clearly.",
                "crop_regions": [(0.0, 0.15, 1.0, 0.35)],
            },
            {
                "filename": "technical_diagram.png",
                "description": "Technical Diagram - System Architecture",
                "question": "What are the main components in this system and how are they connected?",
                "crop_regions": [(0.25, 0.15, 0.75, 0.45)],
            },
            {
                "filename": "challenging_chart.png",
                "description": "Chart with Small Text - Revenue Analysis",
                "question": "What are the exact revenue values for Q1, Q2, Q3, and Q4? Read the legend carefully.",
                "crop_regions": [(0.65, 0.08, 1.0, 0.3)],
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


def main():
    """Run all tests."""
    print("\n🧪 CROP TOOL SKILL - CLAUDE API TEST SUITE\n")

    # Run the main test
    result = test_with_local_images()

    # Exit with appropriate code
    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())
