from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="GuardRail API Wrapper")

POLICY_ENGINE_URL = os.getenv("POLICY_ENGINE_URL", "http://localhost:8000")

class ValidateRequest(BaseModel):
    text: str

@app.post("/validate")
async def validate_text(request: ValidateRequest):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{POLICY_ENGINE_URL}/check",
                json={"agent_output": request.text},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Policy engine unavailable: {e}")

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
