# Crop Tool Test Suite

This directory contains tests for the crop-tool skill.

## Quick Start (No API Key Required!)

### 1. Install Dependencies

```bash
cd tests
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Local Tests

```bash
python3 test_crop_local.py
```

✅ **No API key needed!** This tests all core functionality.

### 3. (Optional) Test with Claude

To test integration with Claude:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
python3 test_crop_tool.py
```

## Tests Included

### Local Tests (No API Key Needed) ✅

**Location:** `test_crop_local.py`

1. **Basic Crop Functionality**
   - Full image crop
   - Quarter crops
   - Center region crops

2. **Coordinate Validation**
   - Out-of-range coordinate rejection
   - Invalid bounding box detection
   - Error message verification

3. **Image Encoding**
   - Base64 PNG encoding
   - Image format conversion (RGBA to RGB)

4. **Generated Test Images**
   - Bar chart cropping
   - Pie chart cropping
   - Table document cropping
   - Technical diagram cropping

5. **Various Image Sizes**
   - Small images (100×100)
   - Medium images (500×300)
   - Large images (1000×1000)
   - Non-square images (200×600)

### Integration Tests (Requires API Key)

**Location:** `test_crop_tool.py`

1. **Coordinate Normalization** (also in local tests)
   - Tests the 0-1 coordinate system
   - Verifies pixel conversion
   - Tests edge cases

2. **FigureQA Integration** (requires ANTHROPIC_API_KEY)
   - Loads real chart from FigureQA dataset
   - Asks Claude to analyze with crop tool
   - Verifies Claude uses the crop tool correctly
   - Tests full end-to-end workflow

## Test Structure

```
tests/
├── README.md                    ← You are here
├── requirements.txt             ← Python dependencies
├── .gitignore                   ← Excludes venv, test_images
├── test_crop_local.py           ← Local tests (generates images on-the-fly)
├── test_crop_tool.py            ← Claude integration tests
├── generate_test_images.py      ← Image generator utility
├── test_images/                 ← GENERATED (not in git)
│   ├── bar_chart.png            ← Auto-generated when tests run
│   ├── pie_chart.png            ← Auto-generated when tests run
│   ├── table_document.png       ← Auto-generated when tests run
│   └── technical_diagram.png    ← Auto-generated when tests run
├── fixtures/                    ← For custom test images (optional)
│   ├── .gitkeep                 ← Keeps folder in git
│   └── README.md                ← How to add custom images
├── venv/                        ← Virtual environment (created by pip, not in git)
└── __pycache__/                 ← Python cache (not in git)
```

**Key Point:** `test_images/` is **generated at runtime** and **NOT checked into git**.
- First run: Tests generate all 4 images
- Subsequent runs: Tests regenerate them (overwrites)
- This keeps the repo clean and lightweight

## How Test Images Work

**Important:** Test images are **generated on-the-fly**, NOT stored in git.

### First Run
```bash
python3 test_crop_local.py
```
→ Calls `generate_test_images.py` → Creates `test_images/` folder with 4 PNGs

### Subsequent Runs
```bash
python3 test_crop_local.py
```
→ Regenerates images in `test_images/` (overwrites previous)

### For Your PR
- ✅ Don't commit `test_images/` folder
- ✅ It's already in `.gitignore`
- ✅ Reviewers will see images auto-generated when they run tests

This approach:
- Keeps repo lightweight
- No large image files
- Tests are self-contained
- Perfect for public contribution ✅

---

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
