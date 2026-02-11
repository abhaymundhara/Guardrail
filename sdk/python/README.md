# Guardrail Python SDK

## Installation

```bash
pip install -r requirements.txt
```

Or from PyPI (coming soon):
```bash
pip install guardrail-sdk
```

## Quick Start

```python
from guardrail import GuardrailClient

# Initialize client
client = GuardrailClient(api_url="http://localhost:8001")

# Validate text
result = client.validate("Your text here")

if result['allowed']:
    print("✓ Text passed validation")
else:
    print(f"✗ Violations: {result['violations']}")
    print(f"Confidence: {result['confidence_score']}")

# Don't forget to close
client.close()
```

## Async Usage

```python
import asyncio
from guardrail import GuardrailClient

async def main():
    client = GuardrailClient()
    result = await client.validate_async("Your text here")
    print(result)

asyncio.run(main())
```

## API Methods

### `validate(text: str) -> Dict`
Synchronous validation. Returns:
- `allowed` (bool): Whether text passed all policies
- `violations` (list): Policy violations detected
- `confidence_score` (float): Confidence in the result

### `validate_async(text: str) -> Dict`
Asynchronous validation. Same response format as `validate()`.

### `close()`
Close the HTTP client connection.

## Configuration

Set custom API endpoint:
```python
client = GuardrailClient(api_url="http://your-server.com:8001")
```

## Error Handling

```python
try:
    result = client.validate(text)
except httpx.ConnectError:
    print("Failed to connect to policy engine")
except Exception as e:
    print(f"Validation error: {e}")
```

## Development

Install dev dependencies:
```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio
```

Run tests:
```bash
pytest tests/
```

---
