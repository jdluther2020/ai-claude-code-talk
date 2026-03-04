"""
Example usage of the crop tool for image analysis.

This demonstrates various ways to use the crop tool to analyze images
by examining specific regions in detail.
"""

from crop_tool import ask_with_crop_tool, analyze_image_with_crops
from PIL import Image


# Example 1: Simple chart analysis
def example_chart_analysis():
    """Analyze a chart and extract key values."""
    print("Example 1: Chart Analysis")
    print("-" * 50)

    # Load a chart image
    image = Image.open("chart.png")

    # Ask Claude to analyze it
    answer = ask_with_crop_tool(
        image=image,
        question="What are the values shown in the legend? List each value with its color.",
    )

    print("Claude's analysis:")
    print(answer)
    print()


# Example 2: Document data extraction
def example_document_extraction():
    """Extract structured data from a document image."""
    print("Example 2: Document Data Extraction")
    print("-" * 50)

    image = Image.open("invoice.png")

    answer = ask_with_crop_tool(
        image=image,
        question="Extract all line items with amounts from the table. Format as: item | quantity | unit_price | total",
    )

    print("Claude's analysis:")
    print(answer)
    print()


# Example 3: Technical diagram analysis
def example_diagram_analysis():
    """Analyze a technical diagram and identify components."""
    print("Example 3: Technical Diagram Analysis")
    print("-" * 50)

    image = Image.open("architecture.png")

    system_prompt = (
        "You are a technical architect. Provide precise analysis of system diagrams. "
        "Crop specific regions to examine details carefully."
    )

    answer = ask_with_crop_tool(
        image=image,
        question="List all components in this architecture diagram and describe their connections.",
        system_prompt=system_prompt,
    )

    print("Claude's analysis:")
    print(answer)
    print()


# Example 4: Multiple questions about one image
def example_multi_question():
    """Ask multiple questions about the same image."""
    print("Example 4: Multi-Question Analysis")
    print("-" * 50)

    image = Image.open("dashboard.png")

    questions = [
        "What is the overall layout and structure of this dashboard?",
        "What metrics are displayed in the top section?",
        "What trends are shown in the time series chart?",
        "What is the status of the alerts or KPIs?",
    ]

    results = analyze_image_with_crops(image, questions)

    for i, (question, answer) in enumerate(results.items(), 1):
        print(f"Q{i}: {question}")
        print(f"A: {answer}\n")


# Example 5: Detailed comparison task
def example_detailed_comparison():
    """Compare multiple elements in a complex image."""
    print("Example 5: Detailed Comparison")
    print("-" * 50)

    image = Image.open("comparison_chart.png")

    system_prompt = (
        "You are an analytical expert. When asked to compare values or elements, "
        "crop specific regions to examine each element in detail, then provide a precise comparison."
    )

    answer = ask_with_crop_tool(
        image=image,
        question="Compare the values across all categories. Crop each category region to read precise values. "
        "Then rank them from highest to lowest.",
        system_prompt=system_prompt,
    )

    print("Claude's analysis:")
    print(answer)
    print()


# Example 6: Reading small text
def example_small_text():
    """Extract small text from images - a key use case for crop tool."""
    print("Example 6: Small Text Extraction")
    print("-" * 50)

    image = Image.open("document.png")

    answer = ask_with_crop_tool(
        image=image,
        question="Read all the footnotes and small print text at the bottom of the page. "
        "Crop the bottom region to ensure you can read clearly.",
    )

    print("Claude's analysis:")
    print(answer)
    print()


# Example 7: Step-by-step analysis with guidance
def example_guided_analysis():
    """Guide Claude through a step-by-step analysis."""
    print("Example 7: Guided Step-by-Step Analysis")
    print("-" * 50)

    image = Image.open("complex_report.png")

    answer = ask_with_crop_tool(
        image=image,
        question="Analyze this report step by step:\n"
        "1. First, identify and crop the title region. What is the document about?\n"
        "2. Next, crop the executive summary section. What are the key points?\n"
        "3. Then, crop the data tables. What are the main metrics?\n"
        "4. Finally, crop the conclusions section. What are the recommendations?",
    )

    print("Claude's analysis:")
    print(answer)
    print()


# Example 8: Handling images from URLs or bytes
def example_flexible_input():
    """Show different ways to provide images."""
    print("Example 8: Flexible Input Methods")
    print("-" * 50)

    # Method 1: File path
    answer1 = ask_with_crop_tool(
        image="chart.png", question="What values are in this chart?"
    )
    print("From file path: ✓")

    # Method 2: PIL Image
    image = Image.open("chart.png")
    answer2 = ask_with_crop_tool(
        image=image, question="What values are in this chart?"
    )
    print("From PIL Image: ✓")

    # Method 3: Bytes dict (from datasets, etc.)
    # answer3 = ask_with_crop_tool(
    #     image={"bytes": image_bytes},
    #     question="What values are in this chart?"
    # )
    # print("From bytes dict: ✓")

    print("\nAll methods work!")
    print()


# Example 9: Custom model and parameters
def example_custom_params():
    """Use custom models and parameters."""
    print("Example 9: Custom Parameters")
    print("-" * 50)

    image = Image.open("chart.png")

    # Use a specific model
    answer = ask_with_crop_tool(
        image=image,
        question="Provide a detailed analysis of this image.",
        model="claude-opus-4-6",  # Latest model
    )

    print("Using claude-opus-4-6: ✓")
    print(answer)
    print()


# Example 10: Real-world FigureQA dataset
def example_figureqa():
    """Example using the FigureQA dataset."""
    print("Example 10: FigureQA Dataset")
    print("-" * 50)

    try:
        from datasets import load_dataset

        # Load a sample from FigureQA
        dataset = load_dataset("vikhyatk/figureqa", split="train", streaming=True)
        example = next(iter(dataset))

        image = example["image"]
        question = example["qa"][0]["question"]

        print(f"Question: {question}\n")

        answer = ask_with_crop_tool(
            image=image,
            question=question,
        )

        print(f"Claude's answer: {answer}")
        print()

    except ImportError:
        print(
            "Note: This example requires the datasets library. Install with: pip install datasets"
        )
        print()


# Main entry point
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("CROP TOOL USAGE EXAMPLES")
    print("=" * 50 + "\n")

    # Note: These examples assume you have the image files
    # In real usage, replace filenames with your actual images

    print("Available examples:")
    print("1. Chart analysis")
    print("2. Document extraction")
    print("3. Technical diagram analysis")
    print("4. Multiple questions")
    print("5. Detailed comparison")
    print("6. Small text extraction")
    print("7. Guided step-by-step analysis")
    print("8. Flexible input methods")
    print("9. Custom parameters")
    print("10. FigureQA dataset")
    print()

    print("To run an example, uncomment the function call below:\n")

    # Uncomment to run examples:
    # example_chart_analysis()
    # example_document_extraction()
    # example_diagram_analysis()
    # example_multi_question()
    # example_detailed_comparison()
    # example_small_text()
    # example_guided_analysis()
    # example_flexible_input()
    # example_custom_params()
    # example_figureqa()

    print("\nQuick Start:")
    print(
        """
    from crop_tool import ask_with_crop_tool
    from PIL import Image

    # Load your image
    image = Image.open("your_image.png")

    # Ask Claude to analyze it
    answer = ask_with_crop_tool(
        image=image,
        question="What are the key details in this image?"
    )

    print(answer)
    """
    )
