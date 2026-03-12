import streamlit as st
import pandas as pd
from swarmpulse.database import SessionLocal
from swarmpulse.models import EvaluationRun

def main():
    st.set_page_config(page_title="SwarmPulse Dash", layout="wide")
    st.title("SwarmPulse: AI Agent Bug-Hunting Dashboard")

    db = SessionLocal()
    data = db.query(EvaluationRun).all()
    
    if not data:
        st.warning("No evaluation data found. Run some tests first!")
        return

    df = pd.DataFrame([{
        "Provider": r.provider,
        "Model": r.model_name,
        "Engine": r.engine_target,
        "Accuracy": r.accuracy_score,
        "Latency (ms)": r.latency_ms,
        "Cost ($)": r.cost_usd,
        "Time": r.timestamp
    } for r in data])

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Accuracy", f"{df['Accuracy'].mean():.2%}")
    col2.metric("Avg Latency", f"{df['Latency (ms)'].mean():.0f}ms")
    col3.metric("Total Spends", f"${df['Cost ($)'].sum():.4f}")

    st.subheader("Model Performance Comparison")
    st.line_chart(df.pivot_table(index='Time', columns='Model', values='Accuracy'))

    st.subheader("Raw Telemetry")
    st.dataframe(df)

if __name__ == "__main__":
    main()
