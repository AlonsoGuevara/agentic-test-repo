
<div align="center">

```
 ██████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
██║     ███████║█████╗  █████╗
██║     ██╔══██║██╔══╝  ██╔══╝
╚██████╗██║  ██║██║     ███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝
```

# ☕ Agentic CAFE

### *Collaborative Agentic Framework for Engineers*

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-ff69b4?style=for-the-badge&logo=github&logoColor=white)](COLLABORATORS.md)

> **A modular, extensible Python framework for building collaborative multi-agent AI systems.**
> Engineer your agents to plan, execute, and review — together.

</div>

---

## 🤔 What is Agentic CAFE?

**Agentic CAFE** is a batteries-included, production-grade Python framework designed for engineers who want to build and orchestrate **collaborative multi-agent AI systems** — without the boilerplate.

Rather than wrestling with glue code, CAFE gives you a clean, composable architecture where AI **agents** work as a team: planning, executing, and reviewing complex engineering tasks end-to-end. Think of it as the **conductor** for your AI orchestra — every instrument (agent) knows its part, and CAFE makes sure they play in harmony.

Whether you're building a code-review pipeline, a research assistant swarm, or an autonomous DevOps bot, Agentic CAFE gives you the building blocks to do it right.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧩 **Modular Agent Architecture** | Plug-and-play agents with well-defined interfaces. Build custom agents in minutes. |
| 🎛️ **Built-in Orchestration Engine** | A powerful core engine manages agent lifecycles, task routing, and inter-agent communication. |
| 🔧 **Pluggable Tool Support** | Equip agents with tools (web search, code execution, APIs) using a simple decorator pattern. |
| ⚡ **Async-First Design** | Built from the ground up with `asyncio` — designed for high-throughput, non-blocking agent pipelines. |
| 🔭 **Rich Observability & Logging** | First-class logging, tracing, and structured event streams powered by [`rich`](https://github.com/Textualize/rich). |

---

## 🏗️ Architecture

Agentic CAFE is organized as a clean, layered system — each layer building on the one below it:

```
┌─────────────────────────────────────────┐
│              📋  Tasks                  │  ← High-level goals & workflows
├─────────────────────────────────────────┤
│              🤖  Agents                 │  ← Autonomous actors that plan & act
├─────────────────────────────────────────┤
│              🔧  Tools                  │  ← Capabilities agents can invoke
├─────────────────────────────────────────┤
│           ⚙️  Core Engine               │  ← Orchestration, scheduling, messaging
└─────────────────────────────────────────┘
```

- **Core Engine** — the heart of CAFE. Handles agent registration, task dispatch, event buses, and async scheduling.
- **Agents** — autonomous units of intelligence. Each agent has a role, a set of tools, and a decision loop.
- **Tools** — atomic capabilities (e.g., `search_web`, `run_code`, `call_api`) that agents use to interact with the world.
- **Tasks** — structured descriptions of work. Tasks flow through the orchestration engine and are assigned to the right agents.

---

## 🚀 Getting Started

### Installation

```bash
pip install agentic-cafe
```

### ⚡ Quickstart

Get your first collaborative agent running in under 30 seconds:

```python
import asyncio
from agentic_cafe import AgentCAFE
from agentic_cafe.agents import BaseAgent
from agentic_cafe.core import Task

# 1. Define a custom agent
class ReviewAgent(BaseAgent):
    name = "code-reviewer"
    role = "Reviews code for quality and correctness"

    async def run(self, task: Task) -> str:
        code = task.payload.get("code", "")
        # ... your logic here (call an LLM, run linters, etc.)
        return f"✅ Review complete for task: {task.id}"

# 2. Boot the CAFE framework
async def main():
    cafe = AgentCAFE()
    cafe.register_agent(ReviewAgent())

    task = Task(
        id="review-001",
        description="Review the authentication module",
        payload={"code": "def login(user, pw): ..."},
    )

    result = await cafe.dispatch(task)
    print(result)

asyncio.run(main())
```

### Requirements

- Python **3.11+**
- `pydantic >= 2.0`
- `httpx >= 0.24`
- `rich >= 13.0`

---

## 📁 Project Structure

```
agentic-cafe/
├── 📄 README.md
├── 📄 COLLABORATORS.md
├── 📄 pyproject.toml
├── 📄 requirements.txt
│
├── 📦 src/
│   └── agentic_cafe/
│       ├── __init__.py          # Package entry point & version
│       ├── agents/
│       │   └── __init__.py      # Agent base classes & registry
│       ├── core/
│       │   └── __init__.py      # Orchestration engine & scheduler
│       └── utils/
│           └── __init__.py      # Shared utilities & helpers
│
└── 🧪 tests/
    └── __init__.py
```

---

## 🤝 Contributing

We ❤️ contributions from the community! Whether it's a bug fix, a new agent type, or improved documentation — every contribution counts.

Please read our [**COLLABORATORS.md**](COLLABORATORS.md) for the full guide on how to get involved, our code standards, and how to submit a Pull Request. We follow an inclusive, welcoming approach to collaboration — everyone is welcome at this CAFE. ☕

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ☕ and ❤️ by the Agentic CAFE community.

*"Great engineers don't work alone — they orchestrate."*

</div>
