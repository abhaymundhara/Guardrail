import httpx
from typing import Dict, Any

class GuardrailClient:
    def __init__(self, api_url: str = "http://localhost:8001"):
        self.api_url = api_url
        self.client = httpx.Client()
    
    def validate(self, text: str) -> Dict[str, Any]:
        """Validate text against all policies"""
        response = self.client.post(
            f"{self.api_url}/validate",
            json={"text": text}
        )
        return response.json()
    
    async def validate_async(self, text: str) -> Dict[str, Any]:
        """Async validation"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/validate",
                json={"text": text}
            )
            return response.json()
    
    def close(self):
        self.client.close()

__all__ = ["GuardrailClient"]
