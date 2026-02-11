# Guardrail Deployment Guide

## Prerequisites
- Python 3.10+
- Docker (optional, for containerized deployment)
- Git

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/abhaymundhara/Guardrail.git
cd Guardrail
```

2. Install dependencies:
```bash
cd policy-engine
pip install -r requirements.txt
cd ../sdk/python
pip install -r requirements.txt
```

3. Start the policy engine:
```bash
cd policy-engine
python main.py
```

4. Run SDK examples:
```bash
cd sdk/python
python examples/basic_validation.py
```

## Docker Deployment

Build the image:
```bash
docker build -t guardrail-engine .
```

Run the container:
```bash
docker run -p 8001:8001 guardrail-engine
```

## Production Deployment

1. Set environment variables:
```bash
export GUARDRAIL_POLICY_ENGINE_URL="https://your-domain.com"
export GUARDRAIL_LOG_LEVEL="INFO"
```

2. Use a production ASGI server (Gunicorn):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8001 policy_engine.main:app
```

3. Set up reverse proxy (nginx):
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:8001;
    }
}
```

4. Enable HTTPS with Let's Encrypt (Certbot)

## Monitoring

- Check logs: `tail -f logs/guardrail.log`
- Health endpoint: `GET http://localhost:8001/health`
- Metrics: Coming in v0.2.0

