# SwarmPulse

SwarmPulse is a comprehensive evaluation dashboard and benchmarking suite designed for AI agent swarms specifically tasked with bug-hunting in game engines (Unity, Unreal, Godot). It provides real-time telemetry on model accuracy, execution latency, and per-token cost analysis across various LLM providers.

## Key Features

*   [Multi-Provider Tracking] Native support for OpenAI, Anthropic, and Local LLMs (via Ollama).
*   [Game Engine Specific Metrics] Tracks success rates for shader compilation errors, collision detection bugs, and memory leaks.
*   [Cost Analytics] Calculates real-time burn rates based on token usage.
*   [Swarm Intelligence Monitoring] Visualizes agent collaboration and redundancy in bug discovery.
*   [Extensible Drivers] Easily plug in new game engine interfaces.

## Quick Start

### Prerequisites
*   Python 3.10+
*   SQLAlchemy for metric persistence
*   A valid API key for your chosen provider

### Installation
```bash
git clone https://github.com/username/swarmpulse.git
cd swarmpulse
pip install -e .
```

### Running the Dashboard
```bash
python -m swarmpulse.app
```

## Architecture

SwarmPulse uses a layered architecture:
1.  **Agent Layer**: Swarm agents executing tasks against game engine APIs.
2.  **Telemetry Layer**: Interceptors that capture request/response data.
3.  **Data Layer**: SQLite/PostgreSQL store for historical performance metrics.
4.  **UI Layer**: A Streamlit-based dashboard for visualization.

## Evaluation Metrics

*   **DRR (Detection Rate Ratio)**: Ratio of confirmed bugs found vs. known bugs.
*   **TTR (Time To Reproduce)**: Latency from initial bug claim to reproducible script generation.
*   **CPC (Cost Per Correction)**: Metric combining API costs with success rate.

## Contributing

Please see CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
