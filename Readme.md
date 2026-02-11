# Guardrail: Enterprise AI Firewall

## Overview

Guardrail is a policy enforcement system designed to protect enterprise LLM deployments from safety violations including PII leakage, profanity, and unauthorized actions.

## Architecture

### Core Components

1. **Policy Engine** (Port 8000)
   - Core validation logic
   - Detects: PII, Profanity, Unauthorized Refunds
   - Returns: violations list + confidence scores

2. **API Wrapper** (Port 8001)
   - FastAPI proxy to Policy Engine
   - `/validate` endpoint accepts text input
   - Clean error handling

3. **Python SDK** (In Progress)
   - Developer-friendly client library
   - Easy integration into existing apps

## Quick Start

### Prerequisites

- Python 3.10+
- FastAPI
- httpx

### Installation

```bash
pip install guardrail-sdk
```

### Basic Usage

```python
from guardrail import GuardrailClient

client = GuardrailClient(policy_engine_url="http://localhost:8000")
result = client.validate("Your text here")

if result['allowed']:
    print("Text is safe")
else:
    print(f"Violations: {result['violations']}")
```

## Policy Details

### 1. PII Detection

Detects: SSN, Email, Credit Card, Phone Numbers
Example: "Your SSN is 123-45-6789" → BLOCKED

### 2. Profanity Filter

Detects: Common profanities
Example: "fuck this shit" → BLOCKED

### 3. Financial Limits

Max refund: $100
Example: "I can refund you $150" → BLOCKED

## API Reference

### POST /validate

Request:

```json
{ "text": "string" }
```

Response:

```json
{
  "allowed": boolean,
  "confidence_score": float,
  "violations": ["string"]
}
```

## Development Status

- [x] Policy Engine Core
- [x] API Wrapper
- [ ] Python SDK
- [ ] Dashboard
- [ ] Monitoring & Logging

## Next Steps

- Build Python SDK for easy integration
- Create monitoring dashboard
- Add custom policy support
- Enterprise deployment guides

---

Built with FastAPI, Python, and paranoia about AI safety.
