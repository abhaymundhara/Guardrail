from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import re
from policies import PolicyEngine

app = FastAPI(title="GuardRail Policy Engine")
policy_engine = PolicyEngine()

class PolicyCheckRequest(BaseModel):
    agent_output: str
    context: Optional[Dict] = {}

class PolicyCheckResponse(BaseModel):
    allowed: bool
    violations: List[str]
    confidence_score: float

@app.post("/check", response_model=PolicyCheckResponse)
async def check_policy(request: PolicyCheckRequest):
    result = policy_engine.evaluate(request.agent_output, request.context)
    return PolicyCheckResponse(
        allowed=result["allowed"],
        violations=result["violations"],
        confidence_score=result["confidence"]
    )

@app.get("/health")
async def health():
    return {"status": "healthy"}

if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
