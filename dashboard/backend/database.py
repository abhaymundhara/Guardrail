from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./dashboard.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Violation(Base):
    __tablename__ = "violations"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    text = Column(String)
    violations = Column(JSON)  # Store list of violations
    confidence_score = Column(Float)
    policy_engine = Column(String, default="default")
    status = Column(String) # "blocked" or "allowed"

Base.metadata.create_all(bind=engine)
