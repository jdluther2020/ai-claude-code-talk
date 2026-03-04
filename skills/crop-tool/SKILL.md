---
name: crop-tool
description: Gives Claude the ability to crop and enhance specific regions of an image for detailed analysis, improving accuracy on vision tasks involving small text, charts, legends, and fine details.
---

# Crop Tool

## When to Use
- Reading small text, legends, or axis labels in charts
- Extracting values from dense tables or diagrams
- Any region where initial analysis feels uncertain

## How to Use
Simply ask naturally about the image. Claude decides which regions to examine and handles the cropping automatically — no coordinates or technical input needed from the user.

```
"Read the values in the legend."
"What does the small text in the bottom section say?"
"Compare the metrics across all three columns."
```

## Skill Mechanics
See [Giving Claude a crop tool for better image analysis](https://platform.claude.com/cookbook/multimodal-crop-tool) for a detailed understanding of the mechanics.

In addition to cropping, this skill enhances the extracted region further:
- **2x upscale** — using LANCZOS resampling for maximum quality
- **1.4x contrast boost** — makes text and edges pop
- **1.3x sharpness boost** — reduces blur introduced by upscaling

### How Claude Must Invoke the Tool

**IMPORTANT:** Always use the skill's `crop_tool.py` CLI via Bash — do NOT write your own PIL/image-processing code.

```bash
python3 /Users/jdl/.claude/skills/crop-tool/crop_tool.py \
  <image_path> <x1> <y1> <x2> <y2> [--output <out_path>]
```

- Coordinates are **normalized (0–1)**, where `(0,0)` is top-left and `(1,1)` is bottom-right
- The script prints the output file path; read that file with the Read tool to view the cropped region
- Iterate across regions as needed until the question is fully answered

**Example:**
```bash
python3 /Users/jdl/.claude/skills/crop-tool/crop_tool.py \
  chart.png 0.5 0.2 1.0 0.65 --output /tmp/legend_crop.png
```

---
*For full documentation see [README.md](README.md).*
