# Guardrail Architecture

## System Design

```
User Input
    ↓
API Wrapper (/validate)
    ↓
Policy Engine (/check)
    ↓
[PII Detector] [Profanity Filter] [Financial Rules]
    ↓
Violations List + Confidence Score
    ↓
Response (allowed: true/false)
```

## Component Details

### Policy Engine (Port 8000)
- **Language**: Python + FastAPI
- **Core Logic**: Multi-policy validation
- **Policies**:
  - PII Leakage Detection
  - Profanity Filtering
  - Unauthorized Refund Blocking
- **Response**: JSON with violations array and confidence scores

### API Wrapper (Port 8001)
- **Language**: Python + FastAPI
- **Role**: Passthrough validator to Policy Engine
- **Endpoint**: POST /validate
- **Error Handling**: Returns 503 if Policy Engine unavailable

### Python SDK (Planned)
- **Role**: Developer-friendly client library
- **Features**:
  - Sync and async clients
  - Built-in retry logic
  - Custom policy support
  - Batching API calls

## Data Flow

1. Client sends text to API Wrapper
2. Wrapper validates against Policy Engine
3. Policy Engine runs all policies in parallel
4. Returns violations + confidence score
5. Wrapper returns result to client

## Deployment

### Local Development
```bash
# Terminal 1: Policy Engine
cd guardrail-core
python main.py

# Terminal 2: API Wrapper
cd api-wrapper
python main.py

# Terminal 3: Tests
python test_suite.py
```

### Production (TBD)
- Docker containerization
- Kubernetes deployment
- Load balancing
- Monitoring & alerting

## Testing Strategy
- Unit tests for each policy
- Integration tests for API wrapper
- Load tests for performance
- Edge case validation

---
