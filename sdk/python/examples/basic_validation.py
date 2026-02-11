#!/usr/bin/env python3
"""Basic validation example"""
from guardrail import GuardrailClient

def main():
    # Initialize client
    client = GuardrailClient(api_url="http://localhost:8001")
    
    # Test cases
    test_cases = [
        "This is a safe message",
        "My SSN is 123-45-6789",
        "I can refund you $500",
        "This is fucking bullshit",
    ]
    
    print("Running validation tests...\n")
    
    for text in test_cases:
        result = client.validate(text)
        status = "✓ PASS" if result['allowed'] else "✗ FAIL"
        print(f"{status}: {text}")
        if not result['allowed']:
            print(f"  Violations: {result['violations']}")
            print(f"  Confidence: {result['confidence_score']:.2f}\n")
    
    client.close()

if __name__ == "__main__":
    main()
