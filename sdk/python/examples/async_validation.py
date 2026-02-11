#!/usr/bin/env python3
"""Async validation example"""
import asyncio
from guardrail import GuardrailClient

async def main():
    client = GuardrailClient(api_url="http://localhost:8001")
    
    test_cases = [
        "Safe message",
        "Email: user@example.com",
        "Card: 4532-1234-5678-9010",
    ]
    
    print("Running async validation tests...\n")
    
    for text in test_cases:
        result = await client.validate_async(text)
        status = "✓ PASS" if result['allowed'] else "✗ FAIL"
        print(f"{status}: {text}")
        if not result['allowed']:
            print(f"  Violations: {result['violations']}\n")

if __name__ == "__main__":
    asyncio.run(main())
