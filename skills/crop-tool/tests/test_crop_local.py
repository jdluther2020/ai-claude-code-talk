#!/usr/bin/env python3
"""
Local tests for crop-tool - No API key required!

Tests the crop tool's core functionality using locally-generated test images.
These tests verify that the crop tool works correctly without needing to call Claude.

Run with: python3 test_crop_local.py
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from crop_tool import handle_crop, pil_to_base64, get_pil_image
from PIL import Image
from generate_test_images import generate_all_test_images


def test_basic_crop():
    """Test basic crop functionality."""
    print("\n" + "=" * 70)
    print("TEST 1: Basic Crop Functionality")
    print("=" * 70)

    # Create a simple test image
    image = Image.new("RGB", (200, 200), color="blue")

    # Test full image crop
    result = handle_crop(image, 0.0, 0.0, 1.0, 1.0)

    assert len(result) == 2, "Should return text + image"
    assert result[0]["type"] == "text", "First item should be text"
    assert result[1]["type"] == "image", "Second item should be image"
    assert "200×200px" in result[0]["text"], "Should report correct dimensions"

    print("✅ Full image crop: PASS")

    # Test quarter crop
    result = handle_crop(image, 0.0, 0.0, 0.5, 0.5)
    assert "100×100px" in result[0]["text"], "Should report 100x100"
    print("✅ Quarter crop: PASS")

    # Test center crop
    result = handle_crop(image, 0.25, 0.25, 0.75, 0.75)
    assert "100×100px" in result[0]["text"], "Should report 100x100"
    print("✅ Center crop: PASS")


def test_coordinate_validation():
    """Test coordinate validation."""
    print("\n" + "=" * 70)
    print("TEST 2: Coordinate Validation")
    print("=" * 70)

    image = Image.new("RGB", (100, 100), color="green")

    # Test out of range coordinates
    result = handle_crop(image, -0.1, 0.0, 1.0, 1.0)
    assert "Error" in result[0]["text"], "Should reject negative coordinates"
    print("✅ Reject negative coordinates: PASS")

    result = handle_crop(image, 0.0, 0.0, 1.5, 1.0)
    assert "Error" in result[0]["text"], "Should reject > 1.0 coordinates"
    print("✅ Reject out-of-range coordinates: PASS")

    # Test invalid bounding box
    result = handle_crop(image, 0.5, 0.5, 0.25, 0.75)
    assert "Error" in result[0]["text"], "Should reject x1 >= x2"
    print("✅ Reject invalid x1/x2: PASS")

    result = handle_crop(image, 0.0, 0.5, 1.0, 0.25)
    assert "Error" in result[0]["text"], "Should reject y1 >= y2"
    print("✅ Reject invalid y1/y2: PASS")


def test_image_encoding():
    """Test image encoding to base64."""
    print("\n" + "=" * 70)
    print("TEST 3: Image Encoding")
    print("=" * 70)

    image = Image.new("RGB", (100, 100), color="red")

    # Test base64 encoding
    encoded = pil_to_base64(image)
    assert isinstance(encoded, str), "Should return string"
    assert len(encoded) > 0, "Should return non-empty string"
    assert encoded.startswith("iVBORw0KGgo"), "Should be valid PNG base64"  # PNG header

    print("✅ Base64 encoding: PASS")
    print(f"✅ Encoded size: {len(encoded)} characters")


def test_with_generated_images():
    """Test with generated test images."""
    print("\n" + "=" * 70)
    print("TEST 4: Generated Test Images")
    print("=" * 70)

    # Generate test images if they don't exist
    test_images_dir = Path(__file__).parent / "test_images"
    if not test_images_dir.exists():
        print("Generating test images...")
        generate_all_test_images()

    test_files = {
        "bar_chart.png": [((0.0, 0.8, 1.0, 1.0), "bottom labels")],  # Test x-axis
        "pie_chart.png": [((0.5, 0.0, 1.0, 0.5), "legend")],  # Test legend area
        "table_document.png": [((0.0, 0.15, 1.0, 0.35), "table header")],  # Test table
        "technical_diagram.png": [((0.25, 0.15, 0.75, 0.45), "components")],  # Test center
    }

    for filename, crops in test_files.items():
        image_path = test_images_dir / filename

        if not image_path.exists():
            print(f"⚠️  Skipping {filename} (not found)")
            continue

        image = Image.open(image_path)
        print(f"\n  Testing: {filename} ({image.width}×{image.height}px)")

        for (x1, y1, x2, y2), region in crops:
            result = handle_crop(image, x1, y1, x2, y2)

            assert len(result) == 2, f"Should return text + image for {filename}"
            assert "×" in result[0]["text"], "Should report dimensions"

            # Calculate expected dimensions (same way as crop_tool does it)
            x1_px = int(x1 * image.width)
            x2_px = int(x2 * image.width)
            y1_px = int(y1 * image.height)
            y2_px = int(y2 * image.height)
            width = x2_px - x1_px
            height = y2_px - y1_px
            expected = f"{width}×{height}px"

            assert expected in result[0]["text"], f"Should report {expected} for {region}"
            print(f"    ✅ {region}: {expected}")


def test_various_image_sizes():
    """Test with various image sizes."""
    print("\n" + "=" * 70)
    print("TEST 5: Various Image Sizes")
    print("=" * 70)

    sizes = [(100, 100), (500, 300), (1000, 1000), (200, 600)]

    for width, height in sizes:
        image = Image.new("RGB", (width, height), color="yellow")

        # Crop center
        result = handle_crop(image, 0.25, 0.25, 0.75, 0.75)

        expected_width = int(0.5 * width)
        expected_height = int(0.5 * height)
        expected = f"{expected_width}×{expected_height}px"

        assert expected in result[0]["text"], f"Should handle {width}×{height}"
        print(f"✅ {width}×{height} → center crop {expected}: PASS")


def main():
    """Run all local tests."""
    print("\n" + "=" * 70)
    print("🧪 CROP TOOL - LOCAL TEST SUITE (NO API KEY NEEDED)")
    print("=" * 70)

    try:
        test_basic_crop()
        test_coordinate_validation()
        test_image_encoding()
        test_with_generated_images()
        test_various_image_sizes()

        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED")
        print("=" * 70)
        print("\nThe crop tool's core functionality works correctly!")
        print("\nNext steps:")
        print("  1. Set ANTHROPIC_API_KEY=... to test with Claude")
        print("  2. Run test_crop_tool.py for full end-to-end testing")
        print("=" * 70 + "\n")
        return 0

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
