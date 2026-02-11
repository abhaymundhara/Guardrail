<div align="center">

# Guardrail: Enterprise AI Firewall

<img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.Guardrail&style=for-the-badge&color=00d4ff" alt="Views">

**Guardrail is a policy enforcement system designed to protect enterprise LLM deployments from safety violations including PII leakage, profanity, and unauthorized actions.**

</div>


### Core Components

1. **Policy Engine** (Port 8000)
   - Core validation logic
   - Detects: PII, Profanity, Unauthorized Refunds
   - Returns: violations list + confidence scores

2. **API Wrapper** (Port 8001)
   - FastAPI proxy to Policy Engine
   - `/validate` endpoint accepts text input
   - Clean error handling

3. **Python SDK** (v0.1.0)
   - Developer-friendly client library
   - Easy integration into existing apps
   - Fully tested and functional

## Quick Start

### Prerequisites

- Python 3.10+
- FastAPI
- httpx

### Installation

```bash
pip install -e .
```

### Basic Usage

```python
from guardrail import GuardrailClient

client = GuardrailClient(policy_engine_url="http://localhost:8001")
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

## Test Results (v0.1.0)

End-to-end SDK testing completed successfully:

✓ PASS: Safe message validation
✓ PASS: PII detection (SSN)
✓ PASS: Unauthorized refund detection
✓ PASS: Profanity filtering

All policies functioning correctly with proper violation detection and reporting.

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
- [x] Python SDK (v0.1.0)
- [x] End-to-end Testing
- [ ] Dashboard
- [ ] Monitoring & Logging
- [ ] Custom Policy Support

## Documentation

- [Deployment Guide](docs/DEPLOYMENT.md)
- [Contributing Guide](docs/CONTRIBUTING.md)

## Next Steps

- Build monitoring dashboard
- Add custom policy support
- Enterprise deployment automation
- Performance optimization

---

Built with FastAPI, Python, and paranoia about AI safety.
