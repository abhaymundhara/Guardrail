from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import httpx
import os

app = FastAPI(title="GuardRail API Wrapper")

POLICY_ENGINE_URL = os.getenv("POLICY_ENGINE_URL", "http://localhost:8000")
POKE_AGENT_URL = os.getenv("POKE_AGENT_URL")
TOMO_AGENT_URL = os.getenv("TOMO_AGENT_URL")

class AgentRequest(BaseModel):
    task: str
    context: Optional[Dict] = {}

class AgentResponse(BaseModel):
    agent: str
    output: str
    policy_status: str

@app.post("/execute", response_model=AgentResponse)
async def execute_task(request: AgentRequest):
    poke_response = await call_agent(POKE_AGENT_URL, request.task, request.context)
    policy_result = await validate_output(poke_response)
    
    if not policy_result["allowed"]:
        raise HTTPException(
            status_code=400,
            detail=f"Policy violations: {policy_result['violations']}"
        )
    
    return AgentResponse(
        agent="poke",
        output=poke_response,
        policy_status="approved"
    )

@app.post("/review")
async def review_output(output: str):
    review = await call_agent(TOMO_AGENT_URL, f"Review this: {output}", {})
    return {"review": review}

async def call_agent(agent_url: str, task: str, context: Dict) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{agent_url}/process",
            json={"task": task, "context": context},
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()["output"]

async def validate_output(output: str) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{POLICY_ENGINE_URL}/check",
            json={"agent_output": output},
            timeout=10.0
        )
        response.raise_for_status()
        return response.json()

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)