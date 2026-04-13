#!/usr/bin/env python3
"""
Crop Tool — Amazon Bedrock Access Verification

Quick smoke test to confirm AWS credentials and Bedrock model access
are working before running the full test suite (test_crop_bedrock.py).

Run with: python3 verify_bedrock.py
"""

import os
import sys

import boto3

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
BEDROCK_MODEL_HAIKU = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
BEDROCK_MODEL = os.environ.get("BEDROCK_MODEL", BEDROCK_MODEL_HAIKU)

print(f"Verifying Bedrock access...")
print(f"  Region : {AWS_REGION}")
print(f"  Model  : {BEDROCK_MODEL}\n")

client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

try:
    response = client.converse(
        modelId=BEDROCK_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {"text": "Reply with exactly: 'Crop tool on Bedrock — ready.'"},
                ],
            }
        ],
    )
    reply = response["output"]["message"]["content"][0]["text"]
    print(f"✅ {reply}")
except Exception as e:
    print(f"❌ Failed: {e}")
    print("\nTroubleshooting:")
    print("  - Run `aws sts get-caller-identity` to verify credentials")
    print("  - Check Bedrock model access in the AWS Console")
    print(f"  - Confirm region '{AWS_REGION}' is correct (override with AWS_REGION=...)")
    sys.exit(1)
