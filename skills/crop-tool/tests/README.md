# Crop Tool Test Suite

This directory contains tests for the crop-tool skill.

## Quick Start

### 1. Install Dependencies

```bash
cd tests
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set API Key

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### 3. Run Tests

```bash
python3 test_crop_tool.py
```

## Tests Included

### Unit Tests

**Location:** `test_crop_tool.py`

1. **Coordinate Normalization** ✅
   - Tests the 0-1 coordinate system
   - Verifies pixel conversion
   - Tests edge cases (full image, quarters, center)
   - Tests error handling (invalid coords)

2. **FigureQA Integration** (requires API key)
   - Loads chart from FigureQA dataset
   - Asks Claude to analyze with crop tool
   - Verifies Claude uses the crop tool
   - Tests end-to-end workflow

3. **Local Image Analysis** (optional)
   - Tests with local image files
   - Useful for custom chart testing

## Test Structure

```
tests/
├── README.md                    ← You are here
├── requirements.txt             ← Python dependencies
├── test_crop_tool.py            ← Main test suite
├── fixtures/                    ← Test data
│   ├── sample_chart.png         ← Optional test image
│   └── README.md                ← Fixture documentation
└── venv/                        ← Virtual environment (created by pip)
```

## Running Individual Tests

### Just Coordinate Tests (no API key needed)

```bash
python3 -c "
import sys
sys.path.insert(0, '..')
from test_crop_tool import test_normalized_coordinates
test_normalized_coordinates()
"
```

### FigureQA Test (requires API key)

```bash
# Set API key first
export ANTHROPIC_API_KEY=...

# Run test
python3 test_crop_tool.py
```

## Expected Output

### Successful Run

```
🧪 CROP TOOL SKILL TEST SUITE

Test 1/3: Coordinate Normalization
======================================================================
✅ Full image: PASS
✅ Top-left quarter: PASS
✅ Center square: PASS
✅ Right half: PASS

Testing error handling...
✅ x1 > x2: Correctly rejected
✅ y1 > y2: Correctly rejected
✅ Out of range: Correctly rejected

Test 2/3: FigureQA Dataset Analysis
======================================================================
📊 Test Chart Question: Is Pale Green the minimum?
✅ Claude's Answer: ...

Test 3/3: Local Image File
======================================================================
⚠️ No local test image found
(This is optional - you can add test images to fixtures/)

======================================================================
TEST SUMMARY
======================================================================
✅ Coordinate normalization: PASS
✅ FigureQA analysis: PASS
⚠️ Local image analysis: SKIPPED
======================================================================

✅ OVERALL: PASSED
```

## Test Coverage

| Component | Test | Status |
|-----------|------|--------|
| Coordinate normalization | Unit | ✅ |
| Pixel conversion | Unit | ✅ |
| Error handling | Unit | ✅ |
| Crop execution | Integration | ✅ |
| Claude integration | E2E | ✅ |
| Image encoding | Unit | ✅ |
| Tool use loop | Integration | ✅ |

## Adding Custom Tests

### Test a Local Image

1. Add image to `fixtures/` folder
2. Run test:

```python
from crop_tool import ask_with_crop_tool
from PIL import Image

image = Image.open("fixtures/your_chart.png")
answer = ask_with_crop_tool(
    image=image,
    question="What values are in this chart?"
)
print(answer)
```

### Test a Specific Scenario

```python
from crop_tool import ask_with_crop_tool

# Your custom scenario
image_path = "fixtures/invoice.png"
question = "Extract all line items and amounts"

answer = ask_with_crop_tool(image_path, question)
print(answer)
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'anthropic'"

**Fix:** Install dependencies
```bash
pip install -r requirements.txt
```

### "Could not resolve authentication method"

**Fix:** Set API key
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### "Could not resolve authentication method" (Windows)

**Fix:** Use Windows environment variable syntax
```cmd
set ANTHROPIC_API_KEY=your_api_key_here
```

### Datasets are slow to download

**Why:** First run downloads FigureQA dataset (~300MB)

**Speed up:** Set HuggingFace token
```bash
export HF_TOKEN=your_hf_token_here
```

### "CUDA out of memory" or performance issues

**Fix:** The crop tool doesn't require GPU - run on CPU if needed
```bash
export CUDA_VISIBLE_DEVICES=""
```

## Contributing Tests

When adding new tests:

1. Add to `test_crop_tool.py`
2. Follow existing test patterns
3. Include docstrings
4. Test both success and failure cases
5. Update this README
6. Run full test suite before submitting

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test Crop Tool

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - run: |
          cd skills/crop-tool/tests
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
          python test_crop_tool.py
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Performance Notes

- **Coordinate tests:** < 1 second
- **FigureQA test:** 10-30 seconds (Claude API call)
- **Full suite:** 15-45 seconds depending on API latency

## Related Documentation

- [Crop Tool README](../README.md) — Usage guide
- [Crop Tool SKILL.md](../SKILL.md) — Skill definition
- [Examples](../example.py) — Usage examples

---

**Questions or issues?** Check the main README or run tests with `-v` flag for verbose output.
