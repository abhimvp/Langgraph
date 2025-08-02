# Building Ambient Agents with LangGraph

- An **`ambient agent`** is an AI system that operates continuously in the background, monitoring for specific events or conditions and automatically taking action without direct user prompts. Unlike traditional chat-bots, ambient agents don't require a user to initiate a conversation; they are triggered by events and can perform tasks autonomously.
- Good article to read through about [Ambient Intelligence](https://www.amazon.science/blog/ambient-intelligence-will-accelerate-advancements-in-general-ai)

## Course Reference

This project is based on the LangChain Academy course materials available at: [Agents from Scratch](https://github.com/langchain-ai/agents-from-scratch)

**Note**: Rather than directly copy-pasting the course notebooks, I will be approaching this course step by step, building my understanding progressively and implementing concepts in my own way as I learn.

## Overview

This project focuses on creating intelligent [ambient agents using LangGraph](https://academy.langchain.com/courses/ambient-agents), a powerful framework for building stateful, multi-agent applications. Ambient agents are AI systems that operate seamlessly in the background, providing contextual assistance and automation without explicit user commands.

## Learning Objectives

- Understanding the core concepts of LangGraph for agent development
- Building stateful agents that can maintain context across interactions
- Implementing multi-agent workflows and coordination
- Creating ambient intelligence systems that proactively assist users

## Project Structure

This directory contains practical implementations and learning materials for building ambient agents, including:

- Code examples and implementations
- Course notes and key insights
- Hands-on exercises and experiments
- Best practices and design patterns

## Notes and Documentation

This repository serves as a comprehensive learning journal, capturing:

- **Instructor insights**: Direct quotes and explanations from course materials
- **Personal understanding**: My interpretation and comprehension of key concepts
- **Practical applications**: How theoretical concepts translate to real-world implementations
- **Reflection points**: Critical thinking and analysis of core principles

### Module 1: LangGraph 101

#### Core Range of Real-World Tasks

- We'll start exploring what ambient agents are in the first place & how they're different from traditional chat agents
- Preview the Gmail agent that we're going to build together
- Learn about some core concepts of LangGraph → Such as:
  - **Workflows vs Agents**: How you can flexibly combine these two things together
- Get comfortable with the core fundamentals of LangGraph such as:
  - **Nodes | Edges | Graphs** - which will become the core building blocks of our Gmail agent
- We'll see how to use LangChain for integrations - with different model providers:
  - LangSmith for observability & evaluation
  - LangGraph platform for deployment & LangGraph Studio for visual & debugging

#### Key Insights on Chat vs Ambient Agents

**Chat Agent Characteristics:**

- Chat is a familiar user-interaction pattern for agents - where users request something of an agent → which can call various tools & respond to the user with an output
- But there are lot of tasks for which chat isn't quite appropriate →
- Example: many users don't want to actually tell an agent to do something
- They want agent to listen precisely to certain events and respond to them automatically

**Ambient Agent Requirements:**

- Many times, we don't want agents to only handle one request at a time → we want them to handle many events concurrently
- Sometimes we want agents to do work in the background for us & only notify us at specific points like when the work has been done, when they need clarification on something (or) when they want to notify us about something

#### Understanding Ambient Agents - Latency Requirements

- Ambient agents can take longer as they working background & only notify us when needed
- In this course, we're gonna build an Ambient agent that:
  - Can handle emails: we will build an agent that can effectively manage your email inbox
  - It will trigger incoming emails and perform actions like:
    - Chat responses (or) schedule meetings
- Now since these are sensitive tasks, we're gonna also how to use human-in-the-loop to approve certain agent actions
- We'll also introduce memory - so agent learns from feedback over-times

#### Core Concepts Covered

**Central Concepts in Tool Calling:**

- **Workflows**: Make decisions along predefined code path
- **Agent**: Tool calling in a loop

**LangGraph Features:**

- LangGraph has a persistence layer for HTTP client-term memory
- Before this we conducted the fundamentals of what first-
- Look at langgraph-101.ipynb

#### Practical Implementation Summary

**What We Built in `langgraph_101.ipynb`:**

1. **Chat Models & Tool Integration**

   - Set up Google Gemini 2.5-flash model using LangChain's standardized interface
   - Created custom tools using `@tool` decorator (email writing functionality)
   - Implemented tool calling with `bind_tools()` method

2. **Basic Workflow Construction**

   - Built simple state-based workflows using `StateGraph`
   - Defined state schemas with TypedDict for type safety
   - Created nodes as Python functions that process and update state

3. **Agent Implementation**

   - Constructed a tool-calling agent using conditional edges
   - Implemented routing logic with `should_continue()` function
   - Used `MessagesState` for conversation flow management

4. **Advanced Features**

   - **Persistence**: Implemented checkpointing with `InMemorySaver` for conversation continuity
   - **Interrupts**: Built human-in-the-loop functionality using `interrupt()` and `Command` objects
   - **Pre-built Agents**: Utilized LangGraph's `create_react_agent` for rapid prototyping

5. **Observability & Deployment**
   - Integrated LangSmith tracing for monitoring agent execution
   - Explored LangGraph Platform deployment options
   - Visualized graph structures using mermaid diagrams

**Key Technical Learnings:**

- State management through reducers and custom update logic
- Graph compilation and execution patterns
- Thread-based conversation persistence
- Integration patterns with external model providers
- Visual debugging capabilities with LangGraph Studio

## Getting Started

### Prerequisites

- **Python 3.11 or later** is required for optimal compatibility with LangGraph

  ```bash
  python3 --version
  ```

### API Keys Setup

You'll need to obtain the following API keys:

1. **Google API Key**: Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. **LangSmith API Key**: Get your key from [LangSmith](https://smith.langchain.com/) to track agent flows and calls

### Environment Configuration

1. Create a `.env` file in the root directory:

   ```bash
   touch .env
   ```

2. Edit the `.env` file with the following configuration:

   ```env
   LANGSMITH_API_KEY=your_langsmith_api_key
   LANGSMITH_TRACING=true
   LANGSMITH_PROJECT="interrupt-workshop"
   GOOGLE_API_KEY=your_google_api_key
   ```

### Installation

#### Recommended: Using uv (faster and more reliable)

```bash
# Install uv if you haven't already
pip install uv

# Install the package with development dependencies
uv sync --extra dev

# Activate the virtual environment
source .venv/bin/activate
```

## Technologies Used

- **LangGraph**: Framework for building stateful agent workflows
- **Python**: Primary programming language
- **LangChain**: Core components for LLM applications

---

_This is an active learning project - documentation and implementations will be continuously updated as new concepts are explored and mastered._
