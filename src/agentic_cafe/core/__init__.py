"""
agentic_cafe.core — Orchestration engine, task scheduler, and event bus.

This module contains the heart of the Agentic CAFE framework: the core engine
responsible for agent registration, task dispatching, inter-agent messaging,
and async lifecycle management.

Key components (to be implemented):
    - AgentCAFE     : Main framework entry point and orchestrator.
    - Task          : Structured unit of work dispatched to agents.
    - EventBus      : Pub/sub message bus for agent communication.
    - Scheduler     : Async task scheduling and prioritisation.

Typical usage:
    from agentic_cafe.core import Task

    task = Task(id="t-001", description="Analyse logs", payload={})
"""
