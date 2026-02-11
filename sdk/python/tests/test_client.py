import pytest
from guardrail import GuardrailClient

@pytest.fixture
def client():
    return GuardrailClient(api_url="http://localhost:8001")

def test_safe_text(client):
    result = client.validate("This is a safe message")
    assert result['allowed'] == True
    assert result['violations'] == []

def test_pii_detection(client):
    result = client.validate("My SSN is 123-45-6789")
    assert result['allowed'] == False
    assert 'PII' in result['violations']

def test_profanity_detection(client):
    result = client.validate("fuck this shit")
    assert result['allowed'] == False
    assert 'profanity' in result['violations']

def test_refund_limit(client):
    result = client.validate("I can refund you $500")
    assert result['allowed'] == False
    assert 'refund_limit' in result['violations']

def test_confidence_score(client):
    result = client.validate("Test message")
    assert 'confidence_score' in result
    assert 0 <= result['confidence_score'] <= 1
