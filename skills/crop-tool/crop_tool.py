"""
Crop Tool - Enable Claude to zoom into specific image regions for detailed analysis.

This module provides utilities for Claude to examine specific regions of images
using normalized coordinates (0-1), dramatically improving accuracy on vision tasks
involving charts, documents, diagrams, and dense images with small details.
"""

import base64
from io import BytesIO
from typing import Union, List, Dict, Any

from anthropic import Anthropic
from PIL import Image as PILImage


# Tool Definition
CROP_TOOL = {
    "name": "crop_image",
    "description": "Crop an image by specifying a bounding box with normalized coordinates (0-1).",
    "input_schema": {
        "type": "object",
        "properties": {
            "x1": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Left edge of bounding box as normalized 0-1 value, where 0 is the left edge and 1 is the right edge",
            },
            "y1": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Top edge of bounding box as normalized 0-1 value, where 0 is the top edge and 1 is the bottom edge",
            },
            "x2": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Right edge of bounding box as normalized 0-1 value",
            },
            "y2": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Bottom edge of bounding box as normalized 0-1 value",
            },
        },
        "required": ["x1", "y1", "x2", "y2"],
    },
}


def pil_to_base64(image: PILImage.Image) -> str:
    """Convert PIL Image to base64 string for transmission."""
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return base64.standard_b64encode(buffer.getvalue()).decode("utf-8")


def get_pil_image(img: Union[PILImage.Image, Dict[str, Any]]) -> PILImage.Image:
    """Convert various image formats to PIL Image."""
    if isinstance(img, PILImage.Image):
        return img
    if isinstance(img, dict) and "bytes" in img:
        return PILImage.open(BytesIO(img["bytes"]))
    if isinstance(img, str):
        return PILImage.open(img)
    raise ValueError(f"Cannot convert {type(img)} to PIL Image")


def handle_crop(
    image: PILImage.Image, x1: float, y1: float, x2: float, y2: float
) -> List[Dict[str, Any]]:
    """
    Execute image crop with normalized coordinates.

    Args:
        image: PIL Image to crop
        x1: Left edge (0-1)
        y1: Top edge (0-1)
        x2: Right edge (0-1)
        y2: Bottom edge (0-1)

    Returns:
        List of tool result content blocks (text confirmation + cropped image)
    """
    # Validate coordinates
    if not all(0 <= c <= 1 for c in [x1, y1, x2, y2]):
        return [{"type": "text", "text": "Error: All coordinates must be between 0 and 1"}]

    if x1 >= x2 or y1 >= y2:
        return [
            {
                "type": "text",
                "text": "Error: Invalid bounding box (x1 must be < x2 and y1 must be < y2)",
            }
        ]

    # Convert normalized to pixel coordinates
    w, h = image.size
    x1_px = int(x1 * w)
    y1_px = int(y1 * h)
    x2_px = int(x2 * w)
    y2_px = int(y2 * h)

    # Perform crop
    cropped = image.crop((x1_px, y1_px, x2_px, y2_px))

    # Log crop operation
    crop_info = f"[CROP TOOL USED] Region: ({x1:.2f}, {y1:.2f}) to ({x2:.2f}, {y2:.2f}) → {cropped.width}×{cropped.height}px"
    print(crop_info)

    # Return result as text + image
    return [
        {
            "type": "text",
            "text": f"Cropped to region ({x1:.2f}, {y1:.2f}) to ({x2:.2f}, {y2:.2f}): {cropped.width}×{cropped.height}px",
        },
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": pil_to_base64(cropped),
            },
        },
    ]


def ask_with_crop_tool(
    image: Union[PILImage.Image, str, Dict[str, Any]],
    question: str,
    model: str = "claude-opus-4-6",
    client: Anthropic = None,
    system_prompt: str = None,
    max_iterations: int = 10,
) -> str:
    """
    Ask Claude a question about an image, with crop tool available.

    Claude will automatically crop image regions as needed to answer the question.
    Uses normalized coordinates (0-1) so Claude doesn't need to know image dimensions.

    Args:
        image: PIL Image, file path, or bytes dict
        question: Question to ask Claude about the image
        model: Claude model to use (default: opus-4-6)
        client: Anthropic client (creates new one if not provided)
        system_prompt: Optional system prompt for Claude
        max_iterations: Maximum tool use iterations (prevents infinite loops)

    Returns:
        Claude's final answer as string
    """
    # Initialize client if not provided
    if client is None:
        client = Anthropic()

    # Convert image to PIL if needed
    image = get_pil_image(image)

    # Default system prompt
    if system_prompt is None:
        system_prompt = (
            "You are a helpful assistant analyzing images. "
            "Use the crop_image tool to examine specific regions when you need detail. "
            "Provide clear, accurate analysis based on what you observe."
        )

    # Build initial message
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Please analyze this image and answer the following question:\n\n{question}\n\n"
                    "Use the crop_image tool to examine specific regions if you need to see details more clearly.",
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

    # Agentic loop
    iteration = 0
    crops_used = 0
    print(f"\n[ASK_WITH_CROP_TOOL] Starting analysis with crop tool...")

    while iteration < max_iterations:
        iteration += 1

        # Call Claude
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            system=system_prompt,
            tools=[CROP_TOOL],
            messages=messages,
        )

        # If Claude is done (no more tool use), return final answer
        if response.stop_reason != "tool_use":
            # Extract final text response
            print(f"[ASK_WITH_CROP_TOOL] Analysis complete. Total crops used: {crops_used}")
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return "Analysis complete"

        # Process tool calls
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # Execute the crop
                crops_used += 1
                result = handle_crop(image, **block.input)
                tool_results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": result}
                )

        # Add tool results to messages
        messages.append({"role": "user", "content": tool_results})

    # If max iterations reached
    return "Analysis reached maximum iterations limit"


def analyze_image_with_crops(
    image: Union[PILImage.Image, str],
    questions: List[str],
    model: str = "claude-opus-4-6",
) -> Dict[str, str]:
    """
    Ask multiple questions about an image, using crop tool.

    Useful for comprehensive image analysis where you need answers to several questions.

    Args:
        image: PIL Image or file path
        questions: List of questions to ask Claude
        model: Claude model to use

    Returns:
        Dictionary mapping questions to Claude's answers
    """
    client = Anthropic()
    results = {}

    for question in questions:
        answer = ask_with_crop_tool(
            image=image, question=question, model=model, client=client
        )
        results[question] = answer

    return results


# Example usage demonstrating the crop tool
if __name__ == "__main__":
    # Example: Analyze a chart
    print("Crop Tool Example\n")
    print("=" * 50)
    print("\nTo use the crop tool:\n")
    print("1. Basic usage:")
    print(
        """
    from crop_tool import ask_with_crop_tool
    from PIL import Image

    image = Image.open("chart.png")
    answer = ask_with_crop_tool(
        image=image,
        question="What are the exact values shown in the legend?"
    )
    print(answer)
    """
    )

    print("\n2. Multiple questions:")
    print(
        """
    from crop_tool import analyze_image_with_crops

    questions = [
        "What is the main title?",
        "What are the axis labels?",
        "What is the legend?",
    ]
    results = analyze_image_with_crops("chart.png", questions)
    for q, a in results.items():
        print(f"Q: {q}")
        print(f"A: {a}\\n")
    """
    )

    print("\n3. Advanced - Custom system prompt:")
    print(
        """
    answer = ask_with_crop_tool(
        image="diagram.png",
        question="Identify all components",
        system_prompt="You are a technical expert analyzing system diagrams. "
                     "Be precise and thorough."
    )
    """
    )
