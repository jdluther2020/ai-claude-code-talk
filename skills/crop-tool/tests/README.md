# Crop Tool — Test Suite

## Table of Contents
- [Quick Start](#quick-start)
- [Stock Test Images](#stock-test-images)
- [Using Your Own Images](#using-your-own-images)
- [Unit Tests](#unit-tests-for-contributors)
- [Troubleshooting](#troubleshooting)

---

## Quick Start

Run the full test suite against Claude via the API:

```bash
cd tests
export ANTHROPIC_API_KEY=your_api_key_here
python3 test_crop_tool.py
```

The script runs two tests:

1. **Integration test** — analyzes all 5 stock images with Claude + crop tool, reports pass/fail for each
2. **Accuracy comparison** — runs the same question on `challenging_chart.png` twice (with and without crop tool) to demonstrate the improvement

---

## Stock Test Images

Five test images are included in `test_images/` and checked into the repo — no generation needed.

| Image | Description | What It Tests |
|-------|-------------|---------------|
| `bar_chart.png` | Quarterly sales bar chart | Reading bar values and axis labels |
| `pie_chart.png` | Market share pie chart | Identifying segments and percentages |
| `table_document.png` | Sales report table | Extracting rows and values from dense data |
| `technical_diagram.png` | System architecture diagram | Reading component names and connections |
| `challenging_chart.png` | Revenue analysis with small text | The hardest case — small legend text and embedded values |

`challenging_chart.png` is the key test image — it's specifically designed to be difficult to read at full resolution, making it the best demonstration of what the crop tool improves.

---

## Using Your Own Images

To test against your own images, drop them into the `fixtures/` folder and run:

```python
from crop_tool import ask_with_crop_tool
from PIL import Image

image = Image.open("fixtures/your_image.png")
answer = ask_with_crop_tool(
    image=image,
    question="What values are shown in the legend?"
)
print(answer)
```

Any image type works — charts, tables, diagrams, screenshots, documents.

---

## Unit Tests (For Contributors)

To verify the core crop and enhance functions work correctly without an API key:

```bash
python3 test_crop_local.py
```

Covers: basic crop functionality, coordinate validation, image encoding, and enhancement chain across various image sizes. Useful for development and CI/CD.

---

## Troubleshooting

**`Could not resolve authentication method`**
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

**`ModuleNotFoundError`**
```bash
pip install -r requirements.txt
```

---

*For full skill documentation see [README.md](../README.md).*
