from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from database import SessionLocal, Violation, engine
import database
import json

# Create tables
database.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Guardrail Dashboard", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ViolationLog(BaseModel):
    text: str
    violations: List[str]
    confidence_score: float
    status: str

class ViolationResponse(BaseModel):
    id: int
    timestamp: datetime
    text: str
    violations: List[str]
    confidence_score: float
    status: str
    policy_engine: Optional[str] = None
    
    @field_validator("violations", mode="before")
    @classmethod
    def parse_violations(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except:
                return []
        return v or []
    
    model_config = {"from_attributes": True}

# Routes
@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/stats")
async def get_stats():
    db = SessionLocal()
    try:
        total = db.query(Violation).count()
        blocked = db.query(Violation).filter(Violation.status == "blocked").count()
        
        violation_types = {}
        for v in db.query(Violation).all():
            violations_list = v.violations
            if isinstance(violations_list, str):
                try:
                    violations_list = json.loads(violations_list)
                except:
                    violations_list = []
            for vtype in (violations_list or []):
                violation_types[vtype] = violation_types.get(vtype, 0) + 1
        
        return {
            "total_validations": total,
            "total_violations": blocked,
            "violation_breakdown": violation_types
        }
    finally:
        db.close()

@app.get("/violations")
async def get_violations(limit: int = 50):
    db = SessionLocal()
    try:
        violations = db.query(Violation).order_by(Violation.timestamp.desc()).limit(limit).all()
        return {
            "violations": [ViolationResponse.model_validate(v) for v in violations],
            "total": len(violations)
        }
    finally:
        db.close()

@app.post("/violations")
async def log_violation(log: ViolationLog):
    db = SessionLocal()
    try:
        violation = Violation(
            text=log.text,
            violations=json.dumps(log.violations),
            confidence_score=log.confidence_score,
            status="blocked" if log.violations else "allowed"
        )
        db.add(violation)
        db.commit()
        db.refresh(violation)
        return {"status": "logged", "id": violation.id}
    except Exception as e:
        print(f"Error logging violation: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)