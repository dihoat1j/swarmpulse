from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class EvaluationRun(Base):
    __tablename__ = "evaluation_runs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    provider = Column(String)
    model_name = Column(String)
    engine_target = Column(String) # Unity, Unreal, etc.
    
    # Metrics
    accuracy_score = Column(Float)
    latency_ms = Column(Integer)
    token_usage = Column(Integer)
    cost_usd = Column(Float)
    
    # Metadata
    agent_id = Column(String)
    task_category = Column(String) # Physics, Rendering, Scripting
    raw_response = Column(JSON)
