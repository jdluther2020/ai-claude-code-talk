# Crop Tool — Amazon Bedrock Tests (boto3)

Tests the crop-tool skill using **Amazon Bedrock** via the boto3 `converse` API,
mirroring the Anthropic SDK tests in `../test_crop_tool.py`.

## Prerequisites

### 1. AWS credentials
Configure credentials using any standard method:
```bash
aws configure                          # interactive setup
export AWS_ACCESS_KEY_ID=...           # or env vars
export AWS_PROFILE=my-profile          # or named profile
```

### 2. Enable Bedrock model access
In the AWS Console → Bedrock → Model access, enable:
- **Claude Haiku 4.5** (default for these tests)
- **Claude Sonnet 4.6** (optional, for higher accuracy)

> Verify the exact model IDs in your Bedrock console — IDs may vary by region.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
Or from the tests/ parent directory:
```bash
pip install boto3 Pillow
```

### 4. Generate test images (if not already done)
```bash
cd ..
python3 generate_test_images.py
```

---

## Running the Tests

```bash
# Step 1 — Verify AWS credentials and Bedrock model access
python3 verify_bedrock.py
# ✅ Crop tool on Bedrock — ready.

# Step 2 — Run the full test suite
python3 test_crop_bedrock.py
```

### Override model or region via environment variables
```bash
AWS_REGION=us-west-2 python3 test_crop_bedrock.py

BEDROCK_MODEL_HAIKU=us.anthropic.claude-haiku-4-5-20251001-v1:0 \
  python3 test_crop_bedrock.py

BEDROCK_MODEL_SONNET=us.anthropic.claude-sonnet-4-6-20251001-v1:0 \
  python3 test_crop_bedrock.py
```

---

## What the Tests Do

Each stock test image runs through two passes — same methodology as the Anthropic SDK tests:

| Pass | Method |
|------|--------|
| WITHOUT crop tool | Full image sent directly to Claude on Bedrock |
| WITH crop tool | Claude crops and enhances regions via agentic loop |

The challenging chart test (`challenging_chart.png`) checks accuracy against
known expected values to quantify improvement.

---

## Key Differences vs Anthropic SDK Tests

| | Anthropic SDK (`test_crop_tool.py`) | Bedrock (`test_crop_bedrock.py`) |
|-|-------------------------------------|-----------------------------------|
| Client | `anthropic.Anthropic()` | `boto3.client("bedrock-runtime")` |
| API method | `client.messages.create()` | `client.converse()` |
| Image format | base64 string | raw bytes |
| Tool definition | `input_schema` | `inputSchema.json` |
| Stop reason | `response.stop_reason` | `response["stopReason"]` |
| Tool use block | `block.type == "tool_use"` | `"toolUse" in block` |

---

## Files

```
tests/aws/
├── README.md                  # This file
├── requirements.txt           # boto3, Pillow
├── verify_bedrock.py          # Pre-flight: verify AWS credentials + model access
└── test_crop_bedrock.py       # Main test suite
```

Shared test assets are in the parent `tests/` directory:
- `tests/test_images/` — stock test images
- `tests/fixtures/`    — your own images
