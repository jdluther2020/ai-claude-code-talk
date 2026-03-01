---
name: crop-tool
description: Crop specific regions of images for detailed analysis. Enables Claude to zoom into relevant areas for improved vision accuracy.
---

# Crop Tool

## Contents

- [Release Notes](#release-notes) — Version history and changes
- [Overview](#overview) — What this skill does and when to use it
- [Installation](#installation) — How to add crop-tool to Claude Code
- [Why It Matters—Performance Impact](#why-it-matters--performance-impact) — Benefits and best use cases
- [What It Does](#what-it-does) — Core functionality and coordinate system
- [How to Use This Skill](#how-to-use-this-skill) — Practical scenarios and workflows
- [Code Examples](#code-examples) — Ready—to—use code patterns
- [When to Use vs Not Use](#when-to-use-vs-not-use) — Decision guide
- [Tips for Best Results](#tips-for-best-results) — Prompt strategies
- [FAQ](#faq) — Common questions answered
- [Integration with Other Tools](#integration-with-other-tools) — Complementary skills
- [Feedback & Improvements](#feedback--improvements) — Contribute ideas
- [Resources](#resources) — External documentation

---

## Release Notes

- **v1.1.0** (2026-02-27) — Added automatic image enhancement (upscale + contrast + sharpen) and improved logging
- **v1.0.0** (2026-02-15) — Initial release with core crop functionality and normalized coordinates

---

## Overview

Inspired by [Anthropic's crop tool technique](https://platform.claude.com/cookbook/multimodal-crop-tool) documented in [Claude Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), this enhanced crop tool extends the capability beyond simple cropping. It gives Claude the ability to **crop AND zoom into** specific regions of images with automatic enhancement:

- **Crop** — Extract specific regions using normalized coordinates (0-1)
- **Zoom** — Automatically upscale (2x), enhance contrast (1.4x), and sharpen (1.3x)
- **Result** — Dramatically improved accuracy on detail-heavy vision tasks

This makes even small, faint text in the original image readable and analyzable.

---

## Installation

```bash
npx skills add https://github.com/jdluther2020/ai-claude-code-talk --skill crop-tool --global --yes
```

> **Why `--global`?** Crop-tool is a general-purpose vision skill useful across all your projects — not just one. Installing globally makes it available everywhere without repeating the install per project. The `--yes` flag skips all interactive prompts for a clean one-command install.

---

## Why It Matters—Performance Impact

The [crop-tool technique](https://platform.claude.com/cookbook/multimodal-crop-tool) documented by Anthropic improves accuracy on detail-heavy vision tasks. Our enhanced version adds automatic upscaling (2x), contrast enhancement (1.4x), and sharpening (1.3x), providing improvements beyond the baseline crop functionality.

**Best for:**
- Analyzing charts with small legends or axis labels
- Extracting data from documents with tables
- Reading technical diagrams with fine details
- Comparing values across multiple image regions
- Any task requiring precision on image details

---

## What It Does

The crop tool provides Claude with the ability to:

1. **Request crops** — Claude specifies a region using normalized coordinates (0-1)
2. **Execute crops** — Tool extracts the specified region from the image
3. **Analyze details** — Claude examines the cropped region in detail
4. **Iterate** — Claude crops additional regions as needed for complete analysis

### Coordinate System

Uses normalized coordinates (0-1) independent of image dimensions:
- **(0, 0)** = top-left corner
- **(1, 1)** = bottom-right corner
- **(0.5, 0.5)** = center of image

This allows Claude to specify regions without knowing actual pixel dimensions.

---

## How to Use This Skill

### Scenario 1: Reading Small Text

**Task:** Extract values from a chart legend

**How to ask:**
```
"Analyze this chart. Start by examining the legend closely."
```

**What Claude does:**
1. Crops the legend region
2. Reads text in high detail
3. Returns the values with confidence

---

### Scenario 2: Comparing Values

**Task:** Determine which pie slice is largest or compare elements

**How to ask:**
```
"Extract these values. Show me the exact regions you examined."
```

**What Claude does:**
1. Examines full image
2. Crops uncertain regions
3. Shows which areas it examined
4. Provides answer with source

---

### Scenario 3: Multi—section Analysis

**Task:** Extract data from a technical document or compare metrics across sections

**How to ask:**
```
"Compare metrics across all three sections of this report."
```

**What Claude does:**
1. Examines full document layout
2. Crops each relevant section
3. Analyzes each section
4. Synthesizes comparison across regions

---

## Code Examples

Ready to implement crop—tool in your own projects? Check out [`example.py`](./example.py) for 10 working code examples showing:

- **Quick reference patterns** — Copy and modify real working code
- **Different use cases** — Chart analysis, document extraction, diagrams, comparisons
- **Advanced features** — Custom models, system prompts, flexible input methods
- **Real datasets** — FigureQA dataset integration example
- **Starting point** — Adaptable code you can build from immediately

Each example is self—contained and ready to use with your own images.

---

## When to Use vs Not Use

### Use crop tool when:
- ✅ Image contains small text or fine details
- ✅ Need high precision on specific regions
- ✅ Analyzing charts, tables, or documents
- ✅ Multiple focal points in image
- ✅ Data extraction required

### Not needed when:
- ❌ Full image already in focus
- ❌ Large text is readable at full resolution
- ❌ Simple object recognition tasks
- ❌ General scene understanding

---

## Tips for Best Results

1. **Be specific about what you need**
   - ✅ "Read the legend and list all color values"
   - ❌ "Analyze this chart"

2. **Mention if precision matters**
   - ✅ "Extract exact numerical values from this table"
   - ❌ "Look at this table"

3. **Point out relevant regions**
   - ✅ "The legend is in the top right corner"
   - ❌ "Look at the legend"

4. **Let Claude crop iteratively**
   - ✅ "Use crop tool to examine any regions you need detail on"
   - ❌ "Crop to (0.5, 0.5, 1.0, 1.0)" (too prescriptive)

5. **Verify results**
   - ✅ Ask Claude to show which regions it cropped
   - ❌ Trust the result without verification

---

## FAQ

**Q: Do I need to specify crop coordinates?**
A: No! Claude decides what to crop. You just ask questions.

**Q: What image sizes work best?**
A: Works with any size. Crop tool automatically handles normalization.

**Q: Can Claude crop the same region multiple times?**
A: Yes, useful for examining at different "zoom levels" or with different questions.

**Q: Is there a limit to crop operations?**
A: No technical limit. Claude will crop as many regions as needed.

**Q: Works with which Claude models?**
A: Opus 4.5+ recommended. Older models have lower vision accuracy even with cropping.

**Q: Can I use this with other vision skills?**
A: Yes! Crop tool complements pdf, docx, xlsx, and other vision tasks.

**Q: Why is my text still unreadable after cropping?**
A: Extremely faint or low-contrast text has limits. The tool upscales and enhances, but can't fix poor original image quality.

---

## Integration with Other Tools

Works well with:
- **Document tools** (pdf, docx, xlsx) — Extract data from complex layouts
- **Web artifacts** — Analyze UI screenshots
- **Code review** — Examine code snippets in images
- **Any vision task** — Improve accuracy through detail

---

## Feedback & Improvements

Have ideas for improvements? Found a use case where crop tool excels? We'd love your contributions!

**How to contribute:**
- Open an issue for bugs or feature requests
- Submit a PR with enhancements
- Share your use cases and real—world examples

This skill is designed for community contribution to the Anthropic ecosystem.

---

## Resources

- [Claude Cookbook: Crop Tool](https://platform.claude.com/cookbook/multimodal-crop-tool)
- [Claude Prompting best practices - Improved vision capabilities](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#minimizing-hallucinations-in-agentic-coding)
- [FigureQA Dataset - Microsoft Research](https://www.microsoft.com/en-us/research/project/figureqa-dataset/)
- [FigureQA: An Annotated Figure Dataset for Visual Reasoning](https://arxiv.org/abs/1710.07300)
- [Claude API Docs](https://platform.claude.com/docs)

---

**Last Updated:** February 27, 2026
**Status:** Production ready
**Recommended Model:** Claude Opus 4.5+
**Benefits:** The [Anthropic crop-tool technique](https://platform.claude.com/cookbook/multimodal-crop-tool) improves accuracy on detail-heavy tasks. Our enhanced version with automatic image processing provides additional gains beyond the baseline technique.
