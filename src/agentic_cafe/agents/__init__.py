"""
agentic_cafe.agents — Agent base classes, registry, and built-in agent types.

This module provides the foundational abstractions for defining agents within
the Agentic CAFE framework. Agents are autonomous units of intelligence that
receive tasks, decide on a course of action, invoke tools, and produce results.

Typical usage:
    from agentic_cafe.agents import BaseAgent

    class MyAgent(BaseAgent):
        name = "my-agent"
        role = "Does something useful"

        async def run(self, task):
            ...
"""
