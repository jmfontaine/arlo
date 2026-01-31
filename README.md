# Arlo

Arlo is an AI agent whose primary purpose it to be a testing ground for his author to get a deeper understanding of
the inner working of AI agents through hands-on experience building one.

## Installation

```bash
git clone https://github.com/jmfontaine/arlo.git
cd arlo
uv sync
```

## Usage

```bash
uv run python test1.py
```

## Project Rules

- Arlo is a learning project. Education comes before production readiness.
- Arlo is built by its author or by Arlo itself. No other AI agents are used in development.
- Arlo implements AI agent primitives in their simplest correct form. Refinement comes after understanding.
- Arlo is model-agnostic.
- Simplicity is preferred, but not at the cost of clarity or maintainability.
- Python dependencies unrelated to AI are allowed (e.g., Typer for CLI, HTTPX for HTTP). AI and LLM frameworks
    are not (e.g., LangChain, LlamaIndex, CrewAI). The learning happens by building agent patterns from scratch.
    LLM SDKs are the exception as there is no need to reinvent the wheel for API communication.

## Why This Name?

Arlo stands for Arlo Recursively Loops Onward, a nod to the agent loop at its core.

## Disclaimer

There are no guarantees of stability, completeness, or support. Use at your own risk.

## License

Arlo is licensed under the [Apache License 2.0](./LICENSE.txt).
