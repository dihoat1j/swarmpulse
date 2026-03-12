from swarmpulse.agent import BugHunterAgent
from swarmpulse.database import init_db

def run_simulation():
    print("Initializing Database...")
    init_db()
    
    agents = [
        BugHunterAgent("gpt-4", "openai"),
        BugHunterAgent("claude-3-opus", "anthropic"),
        BugHunterAgent("gpt-3.5-turbo", "openai")
    ]
    
    tasks = [
        "Fix phantom forces in rigid body solver",
        "Optimize draw calls for mobile shader",
        "Identifty memory leak in asset uploader",
        "Debug race condition in sound engine"
    ]
    
    print("Starting Swarm Bug-Hunting Simulation...")
    for task in tasks:
        for agent in agents:
            print(f"Agent {agent.model_name} processing: {task}")
            result = agent.run_task(task)
            print(f"Result: {result}")

if __name__ == "__main__":
    run_simulation()
    print("\nSimulation complete. Run 'streamlit run swarmpulse/app.py' to see results.")
