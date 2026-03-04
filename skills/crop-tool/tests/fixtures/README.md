# fixtures/

Place your own images here to test them with the crop tool.

Any `.png`, `.jpg`, `.jpeg`, or `.webp` file dropped in this folder will be automatically picked up by `test_crop_tool.py` and run through the with/without comparison.

```bash
cp ~/my_chart.png fixtures/
python3 test_crop_tool.py
```

**Good candidates:** charts, tables, diagrams, screenshots, invoices — anything with small text or dense detail you want Claude to analyze.

Keep files under 1MB where possible to keep the repo lightweight.
