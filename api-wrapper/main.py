from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from datetime import datetime

app = FastAPI(title="GuardRail API Wrapper")

POLICY_ENGINE_URL = os.getenv("POLICY_ENGINE_URL", "http://localhost:8000")
DASHBOARD_URL = os.getenv("DASHBOARD_URL", "http://localhost:8002")

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
            result = response.json()
            
            # Log to dashboard
            violation_log = {
                "text": request.text,
                "violations": result.get("violations", []),
                "confidence_score": result.get("confidence_score", 0.0),
                "status": "blocked" if result.get("violations") else "allowed"
            }
            
            try:
                await client.post(
                    f"{DASHBOARD_URL}/violations",
                    json=violation_log,
                    timeout=5.0
                )
            except Exception as e:
                print(f"Dashboard logging failed: {e}")
            
            return result
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Policy engine unavailable: {e}")

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
