# Test Fixtures

This folder contains test images and data for testing the crop-tool skill.

## Using Fixtures

### Option 1: Use FigureQA (Default)

The test suite automatically downloads chart images from the FigureQA dataset. No setup needed - just run tests.

```bash
python3 test_crop_tool.py
```

### Option 2: Add Your Own Test Image

Place an image in this folder and the test will detect it:

```bash
# Example: Copy a test chart here
cp ~/my_chart.png fixtures/chart.png

# Re-run tests
python3 test_crop_tool.py
```

**Supported formats:** PNG, JPEG, GIF, WebP

## Creating Test Images

### Option A: Use an Existing Chart

1. Find a chart/diagram online
2. Save as PNG or JPEG
3. Place in `fixtures/` folder

### Option B: Create a Simple Test Chart

```python
from PIL import Image, ImageDraw

# Create a simple test image
image = Image.new('RGB', (400, 300), color='white')
draw = ImageDraw.Draw(image)

# Draw a simple chart
draw.rectangle([50, 50, 350, 250], outline='black')
draw.text((150, 120), "TEST CHART", fill='black')

image.save('fixtures/test_chart.png')
```

### Option C: Use Real Charts from FigureQA

The test suite automatically downloads from FigureQA:
- 100k+ real charts
- Multiple types (bar, pie, line, scatter)
- Automatically used when available

## Test Data Size

| Source | Size | Time | Cost |
|--------|------|------|------|
| FigureQA (default) | ~300MB | First download ~5 min | Free (once) |
| Local images | < 10MB | Instant | Free |
| Custom fixtures | Variable | Depends on API calls | API credits |

## Example Test Image

To test the crop tool yourself, you can use any chart or dense image:

```python
from crop_tool import ask_with_crop_tool
from PIL import Image

# Load your test image
image = Image.open('fixtures/your_chart.png')

# Test the crop tool
answer = ask_with_crop_tool(
    image=image,
    question="What is shown in this chart?"
)

print(answer)
```

## Recommended Test Cases

### 1. Bar Chart
- **What to test:** Comparing bar heights, reading labels
- **Why:** Common use case, tests legend reading

### 2. Pie Chart
- **What to test:** Identifying slices, reading percentages
- **Why:** Requires precision, tests angle/color recognition

### 3. Line Chart
- **What to test:** Reading point values, identifying trends
- **Why:** Tests temporal analysis, x/y axis reading

### 4. Table/Document
- **What to test:** Extracting row/column values
- **Why:** Tests dense text reading

### 5. Technical Diagram
- **What to test:** Identifying components, reading labels
- **Why:** Tests spatial reasoning and detail focus

## Adding Your Test Images

1. Create a subdirectory: `fixtures/my_tests/`
2. Add images there
3. Create a simple test script:

```python
from crop_tool import ask_with_crop_tool
from pathlib import Path

test_dir = Path('fixtures/my_tests')

for image_path in test_dir.glob('*.png'):
    question = "Describe what you see in detail"
    answer = ask_with_crop_tool(image_path, question)
    print(f"{image_path.name}: {answer}\n")
```

## CI/CD Integration

For automated testing, fixtures are handled via:

1. **FigureQA** (online, no storage needed)
2. **GitHub LFS** (for large test images)
3. **URLs** (download on first test run)

```python
# Example: Download test image if needed
import urllib.request
from pathlib import Path

def ensure_fixture(name, url):
    path = Path('fixtures') / name
    if not path.exists():
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(url, path)
    return path
```

## Storage Guidelines

To keep the repo size manageable:

- ✅ Keep fixtures < 1MB each
- ✅ Use FigureQA for large datasets
- ✅ Compress PNGs with `pngquant`
- ❌ Don't commit large image files (use LFS or URLs)

---

**Questions?** See the [Test Suite README](../README.md)
