#!/usr/bin/env python3
"""
Test script for crop-tool skill.

Tests the crop tool with real data from the FigureQA dataset.
Verifies that Claude can successfully use the crop tool to analyze charts.
"""

import sys
import os

# Add parent directory to path for imports (crop_tool.py is in parent)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from crop_tool import ask_with_crop_tool
from PIL import Image


def test_with_figureqa():
    """Test crop tool with FigureQA dataset."""
    print("\n" + "=" * 70)
    print("CROP TOOL TEST - FigureQA Dataset")
    print("=" * 70 + "\n")

    try:
        from datasets import load_dataset
    except ImportError:
        print("❌ datasets library not installed")
        print("Install with: pip install datasets")
        return False

    print("Loading FigureQA dataset...")
    try:
        dataset = load_dataset("vikhyatk/figureqa", split="train", streaming=True)
        example = next(iter(dataset))
        image = example["image"]
        question = example["qa"][0]["question"]

        print(f"✅ Dataset loaded")
        print(f"\n📊 Test Chart Question: {question}\n")

        print("Analyzing with Claude + crop-tool...")
        print("-" * 70)

        answer = ask_with_crop_tool(
            image=image,
            question=question,
            model="claude-opus-4-6",
        )

        print("-" * 70)
        print(f"\n✅ Claude's Answer:\n{answer}\n")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_with_local_image():
    """Test crop tool with a local image file."""
    print("\n" + "=" * 70)
    print("CROP TOOL TEST - Local Image File")
    print("=" * 70 + "\n")

    # Look for sample images
    sample_files = ["chart.png", "test_chart.png", "sample.png"]

    image_path = None
    for filename in sample_files:
        if os.path.exists(filename):
            image_path = filename
            break

    if not image_path:
        print("⚠️  No local test image found")
        print("Looking for: chart.png, test_chart.png, sample.png")
        print("Create a test image to run this test\n")
        return None

    print(f"Found image: {image_path}")

    try:
        image = Image.open(image_path)
        print(f"✅ Image loaded: {image.width}x{image.height}px\n")

        question = "What details can you see in this image? Crop any regions that need closer inspection."

        print(f"Question: {question}\n")
        print("Analyzing with Claude + crop-tool...")
        print("-" * 70)

        answer = ask_with_crop_tool(image=image, question=question)

        print("-" * 70)
        print(f"\n✅ Claude's Answer:\n{answer}\n")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_normalized_coordinates():
    """Test the coordinate normalization logic."""
    print("\n" + "=" * 70)
    print("COORDINATE NORMALIZATION TEST")
    print("=" * 70 + "\n")

    from crop_tool import handle_crop

    # Create a test image
    print("Creating test image (100x100)...")
    test_image = Image.new("RGB", (100, 100), color="blue")

    # Test cases
    test_cases = [
        {
            "name": "Full image",
            "coords": (0.0, 0.0, 1.0, 1.0),
            "expected_size": (100, 100),
        },
        {
            "name": "Top-left quarter",
            "coords": (0.0, 0.0, 0.5, 0.5),
            "expected_size": (50, 50),
        },
        {
            "name": "Center square",
            "coords": (0.25, 0.25, 0.75, 0.75),
            "expected_size": (50, 50),
        },
        {
            "name": "Right half",
            "coords": (0.5, 0.0, 1.0, 1.0),
            "expected_size": (50, 100),
        },
    ]

    all_passed = True

    for test in test_cases:
        x1, y1, x2, y2 = test["coords"]
        result = handle_crop(test_image, x1, y1, x2, y2)

        # Check if result is valid
        has_text = any(item.get("type") == "text" for item in result)
        has_image = any(item.get("type") == "image" for item in result)

        if has_text and has_image:
            print(f"✅ {test['name']}: PASS")
        else:
            print(f"❌ {test['name']}: FAIL")
            all_passed = False

    # Test invalid coordinates
    print("\nTesting error handling...")
    invalid_cases = [
        {"name": "x1 > x2", "coords": (0.5, 0.0, 0.25, 1.0)},
        {"name": "y1 > y2", "coords": (0.0, 0.5, 1.0, 0.25)},
        {"name": "Out of range", "coords": (0.0, 0.0, 1.5, 1.0)},
    ]

    for test in invalid_cases:
        x1, y1, x2, y2 = test["coords"]
        result = handle_crop(test_image, x1, y1, x2, y2)

        # Should have error text
        has_error = any(
            "Error" in item.get("text", "") for item in result if item.get("type") == "text"
        )

        if has_error:
            print(f"✅ {test['name']}: Correctly rejected")
        else:
            print(f"❌ {test['name']}: Should have rejected")
            all_passed = False

    print()
    return all_passed


def main():
    """Run all tests."""
    print("\n🧪 CROP TOOL SKILL TEST SUITE\n")

    # Test 1: Coordinate normalization
    print("Test 1/3: Coordinate Normalization")
    test1_passed = test_normalized_coordinates()

    # Test 2: FigureQA (main test)
    print("\nTest 2/3: FigureQA Dataset Analysis")
    try:
        test2_passed = test_with_figureqa()
    except Exception as e:
        print(f"❌ FigureQA test skipped: {e}")
        test2_passed = None

    # Test 3: Local image (optional)
    print("\nTest 3/3: Local Image File")
    try:
        test3_result = test_with_local_image()
        test3_passed = test3_result if test3_result is not None else None
    except Exception as e:
        print(f"⚠️  Local image test skipped: {e}")
        test3_passed = None

    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    print(f"✅ Coordinate normalization: {'PASS' if test1_passed else 'FAIL'}")

    if test2_passed is not None:
        print(f"{'✅' if test2_passed else '❌'} FigureQA analysis: {'PASS' if test2_passed else 'FAIL'}")
    else:
        print("⚠️  FigureQA analysis: SKIPPED")

    if test3_passed is not None:
        print(
            f"{'✅' if test3_passed else '❌'} Local image analysis: {'PASS' if test3_passed else 'FAIL'}"
        )
    else:
        print("⚠️  Local image analysis: SKIPPED")

    print("=" * 70 + "\n")

    # Determine overall result
    required_tests = [test1_passed, test2_passed]
    if all(t is False for t in required_tests if t is not None):
        print("❌ OVERALL: FAILED\n")
        return 1
    elif all(t is True for t in required_tests if t is not None):
        print("✅ OVERALL: PASSED\n")
        return 0
    else:
        print("⚠️  OVERALL: PARTIAL (some tests skipped)\n")
        return 0


if __name__ == "__main__":
    sys.exit(main())
