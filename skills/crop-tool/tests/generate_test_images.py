"""
Generate test images for crop-tool testing.

Creates realistic test images that demonstrate crop tool use cases:
- Bar chart
- Pie chart
- Document with table
- Technical diagram

These images are used for testing without requiring API calls or external datasets.
"""

import os
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def create_test_images_dir():
    """Ensure test images directory exists."""
    test_images_dir = Path(__file__).parent / "test_images"
    test_images_dir.mkdir(exist_ok=True)
    return test_images_dir


def generate_bar_chart():
    """Generate a simple bar chart for testing."""
    img = Image.new("RGB", (600, 400), color="white")
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((150, 20), "Quarterly Sales", fill="black")

    # Axes
    draw.line([(50, 350), (550, 350)], fill="black", width=2)  # X axis
    draw.line([(50, 50), (50, 350)], fill="black", width=2)  # Y axis

    # Labels
    draw.text((30, 360), "$0", fill="black")
    draw.text((20, 50), "$1000", fill="black")

    # Bars
    data = [("Q1", 200, "blue"), ("Q2", 350, "green"), ("Q3", 275, "orange"), ("Q4", 400, "red")]

    for i, (quarter, value, color) in enumerate(data):
        x_pos = 100 + i * 100
        height = value * 2.8  # Scale to fit

        # Draw bar
        draw.rectangle(
            [(x_pos, 350 - height), (x_pos + 60, 350)],
            fill=color,
            outline="black",
        )

        # Label
        draw.text((x_pos + 10, 360), quarter, fill="black")

    # Legend
    legend_y = 370
    for i, (quarter, _, color) in enumerate(data):
        draw.rectangle([(420 + i * 30, legend_y), (435 + i * 30, legend_y + 10)], fill=color)
        draw.text((440 + i * 30, legend_y), quarter, fill="black")

    test_images_dir = create_test_images_dir()
    img.save(test_images_dir / "bar_chart.png")
    return test_images_dir / "bar_chart.png"


def generate_pie_chart():
    """Generate a simple pie chart for testing."""
    img = Image.new("RGB", (600, 400), color="white")
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((200, 20), "Market Share", fill="black")

    # Draw pie chart using wedges
    center = (150, 200)
    radius = 80

    # Segments (label, percentage, color)
    segments = [("Product A", 30, "red"), ("Product B", 25, "blue"), ("Product C", 20, "green"), ("Product D", 25, "gold")]

    current_angle = 0
    for label, percentage, color in segments:
        # Calculate start and end angles
        angle_span = (percentage / 100) * 360
        start_angle = current_angle
        end_angle = current_angle + angle_span

        # Draw pie slice
        draw.pieslice(
            [
                (center[0] - radius, center[1] - radius),
                (center[0] + radius, center[1] + radius),
            ],
            start=start_angle,
            end=end_angle,
            fill=color,
            outline="black",
        )

        current_angle = end_angle

    # Legend
    legend_x = 320
    legend_y = 80
    for i, (label, percentage, color) in enumerate(segments):
        y = legend_y + i * 30
        draw.rectangle([(legend_x, y), (legend_x + 15, y + 15)], fill=color, outline="black")
        draw.text((legend_x + 25, y), f"{label} ({percentage}%)", fill="black")

    test_images_dir = create_test_images_dir()
    img.save(test_images_dir / "pie_chart.png")
    return test_images_dir / "pie_chart.png"


def generate_table_document():
    """Generate a document image with a table."""
    img = Image.new("RGB", (600, 500), color="white")
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((150, 20), "Sales Report Q4 2024", fill="black")

    # Table header
    headers = ["Product", "Units", "Revenue", "Margin"]
    col_width = 130
    row_height = 30

    for i, header in enumerate(headers):
        x = 50 + i * col_width
        y = 80
        draw.rectangle([(x, y), (x + col_width, y + row_height)], outline="black", width=2)
        draw.text((x + 10, y + 10), header, fill="black")

    # Table data
    data = [
        ("Widget", "1,500", "$45,000", "32%"),
        ("Gadget", "2,200", "$66,000", "28%"),
        ("Doohickey", "900", "$27,000", "35%"),
        ("Thingamajig", "1,200", "$36,000", "30%"),
    ]

    for row_idx, row_data in enumerate(data):
        for col_idx, value in enumerate(row_data):
            x = 50 + col_idx * col_width
            y = 80 + (row_idx + 1) * row_height
            draw.rectangle([(x, y), (x + col_width, y + row_height)], outline="gray", width=1)
            draw.text((x + 10, y + 10), value, fill="black")

    # Footer
    draw.text((50, 450), "Total Revenue: $174,000 | Average Margin: 31.25%", fill="black")

    test_images_dir = create_test_images_dir()
    img.save(test_images_dir / "table_document.png")
    return test_images_dir / "table_document.png"


def generate_technical_diagram():
    """Generate a technical diagram for testing."""
    img = Image.new("RGB", (700, 500), color="white")
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((200, 20), "System Architecture", fill="black")

    # Components
    components = [
        ("Client", 50, 100, "lightblue"),
        ("API Gateway", 250, 100, "lightgreen"),
        ("Database", 450, 100, "lightyellow"),
        ("Cache", 250, 300, "lightcoral"),
    ]

    for label, x, y, color in components:
        draw.rectangle([(x, y), (x + 120, y + 60)], fill=color, outline="black", width=2)
        draw.text((x + 20, y + 20), label, fill="black")

    # Connections
    connections = [
        ((170, 130), (250, 130)),  # Client to API
        ((370, 130), (450, 130)),  # API to DB
        ((310, 160), (310, 300)),  # API to Cache
    ]

    for start, end in connections:
        draw.line([start, end], fill="black", width=2)
        # Arrow
        draw.polygon([(end[0], end[1]), (end[0] - 10, end[1] - 5), (end[0] - 10, end[1] + 5)], fill="black")

    # Labels
    draw.text((180, 115), "HTTP", fill="darkgray")
    draw.text((380, 115), "Query", fill="darkgray")
    draw.text((320, 220), "Redis", fill="darkgray")

    test_images_dir = create_test_images_dir()
    img.save(test_images_dir / "technical_diagram.png")
    return test_images_dir / "technical_diagram.png"


def generate_challenging_chart():
    """Generate a chart where cropping reveals details that are hard to read at full size.

    This is the key test: full image is readable but IMPRECISE,
    cropped legend is PRECISE and ACCURATE.
    """
    img = Image.new("RGB", (1000, 600), color="white")
    draw = ImageDraw.Draw(img)

    # Title (large, readable)
    draw.text((300, 20), "Revenue Analysis - Q1-Q4 2024", fill="black")

    # Draw bars (large, clearly readable)
    data = [("Q1", 125), ("Q2", 250), ("Q3", 187), ("Q4", 312)]

    for i, (quarter, value) in enumerate(data):
        x = 80 + i * 170
        height = value * 1.2

        # Bar (large and clear)
        draw.rectangle([(x, 450 - height), (x + 120, 450)], fill="steelblue", outline="black", width=2)

        # Quarter label (readable)
        draw.text((x + 35, 460), quarter, fill="black")

    # LEGEND - Small text that's readable but requires careful reading
    # Without cropping: Hard to read precisely, easy to make errors
    # With cropping: Crystal clear and accurate
    legend_x = 650
    legend_y = 80

    # Heading
    draw.text((legend_x, legend_y), "Legend (small text - easy to misread):", fill="black")

    # Legend items in SMALL but readable font (this is key!)
    legend_items = [
        ("Q1", "$125K"),
        ("Q2", "$250K"),
        ("Q3", "$187.5K"),
        ("Q4", "$312K"),
    ]

    y_offset = legend_y + 35
    for quarter, value in legend_items:
        # Small but readable text - hard to read accurately at full resolution
        text = f"{quarter}: {value}"
        draw.text((legend_x, y_offset), text, fill="darkslategray")
        y_offset += 25

    # Add some additional info below
    draw.text((legend_x, legend_y + 150), "Total: $874.5K", fill="darkslategray")
    draw.text((legend_x, legend_y + 175), "Growth: +23.5%", fill="darkslategray")

    # Axis labels (normal readable size)
    draw.text((350, 530), "Quarter", fill="black")
    draw.text((30, 200), "Revenue ($K)", fill="black")

    # Add subtle grid lines to make reading harder
    for i in range(50, 451, 50):
        draw.line([(50, i), (550, i)], fill="lightgray", width=1)

    test_images_dir = create_test_images_dir()
    img.save(test_images_dir / "challenging_chart.png")
    return test_images_dir / "challenging_chart.png"


def generate_all_test_images():
    """Generate all test images."""
    print("Generating test images...")

    images = {
        "bar_chart.png": generate_bar_chart(),
        "pie_chart.png": generate_pie_chart(),
        "table_document.png": generate_table_document(),
        "technical_diagram.png": generate_technical_diagram(),
        "challenging_chart.png": generate_challenging_chart(),
    }

    test_images_dir = create_test_images_dir()
    print(f"✅ Test images generated in: {test_images_dir}\n")

    for name, path in images.items():
        size = os.path.getsize(path) / 1024  # KB
        print(f"  ✅ {name} ({size:.1f} KB)")

    return images


if __name__ == "__main__":
    generate_all_test_images()
    print("\nTest images ready for testing!")
