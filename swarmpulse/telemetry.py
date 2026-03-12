import time
import uuid
from typing import Dict, Any
from .database import SessionLocal
from .models import EvaluationRun

class TelemetryTracker:
    def __init__(self, provider: str, model_name: str, engine_target: str):
        self.provider = provider
        self.model_name = model_name
        self.engine_target = engine_target

    def record_run(self, accuracy: float, latency: int, tokens: int, cost: float, meta: Dict[str, Any]):
        db = SessionLocal()
        run = EvaluationRun(
            provider=self.provider,
            model_name=self.model_name,
            engine_target=self.engine_target,
            accuracy_score=accuracy,
            latency_ms=latency,
            token_usage=tokens,
            cost_usd=cost,
            agent_id=str(uuid.uuid4())[:8],
            task_category=meta.get("category", "general"),
            raw_response=meta.get("response", {})
        )
        db.add(run)
        db.commit()
        db.close()

def calculate_cost(tokens: int, provider: str, model: str) -> float:
    # Simplified cost mapping per 1k tokens
    rates = {
        "openai": {"gpt-4": 0.03, "gpt-3.5-turbo": 0.002},
        "anthropic": {"claude-3-opus": 0.015, "claude-3-sonnet": 0.003}
    }
    rate = rates.get(provider, {}).get(model, 0.01)
    return (tokens / 1000) * rate
