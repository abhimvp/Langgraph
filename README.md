# Langgraph

![LangChain Academy](<https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/66e9eba1020525eea7873f96_LCA-big-green%20(2).svg>)

- Master Custom AI Agent creation
- `LangGraph` is an orchestration framework for complex agentic systems and is more low-level and controllable than LangChain agents. On the other hand, `LangChain` provides a standard interface to interact with models and other components, useful for straight-forward chains and retrieval flows.
- `LangGraph Platform` is a platform for deploying AI agents that can scale with production volume. It `offers easy-to-use APIs for managing agent state, memory, and user interactions`— which makes building dynamic experiences more accessible. ‍ Once you're ready to ship to production, use LangGraph Platform to gracefully handle large workloads, with features like retries and cost-efficient execution for reliable performance. LangGraph Platform also includes `LangGraph Studio`, which lets you gain visibility into how agents act, helping you prototype faster.

## Good References to get started

- [langgraph Simplified](https://youtu.be/R-o_a6dvzQM?si=sj8ZmacITyDPAHBM) - Provides fundamental idea one should have when they want to work with langGraph - know what is a graph -> Node and edges -> nodes can be Agents or tools -> Edges can be normal or conditional ones where they connect nodes in a sequential order -> what is a State , prompts ..etc & [code Repo](https://github.com/john-adeojo/graph_websearch_agent)
- Learn from langchain academy about [langgraph](https://academy.langchain.com/courses/intro-to-langgraph) & it's [code repo files](https://github.com/langchain-ai/langchain-academy)

## Langchain Academy - LangGraph

- One type of LLM Application that you can build is an `agent`.You can create an agent by allowing an LLM to determine the control flow of an application.
  - They can automate wide range of tasks that were previously impossible.
  - Also we need more control is often necessary, You might need an agent to always call a specific tool first or to use different prompts based on it's state.
  - **`Here Langgraph solves this problem`** : A Framework for building Agentic and Multi-Agent applications. Apart from langchain , langgraph's core design philosophy is to help developers add better precision and more control into agentic workflows, making them suitable for the complexity of real-world Systems.
  - let's learn to how to use langgraph to build agents that can reliably handle different types of day-to-day tasks that you actually encounter in your work.
- **`Module 1`** : we'll start with the fundamentals of agents & introduce Langgraph and build a few generalist agent architectures.
- **`Module 2`** : we'll learn how to work with MESSAGES to exchange information within your agent, we'll also show how to use memory to save your agent's internal state.
- **`Module 3`** : we'll learn how to add human-in-the-loop to approve specific actions or review your agent's work.
- **`Module 4`** : we'll build this all into a research assistant that can produce customizable knowledge outputs like reports or wikis or summaries using various types of tools you give it, such as web search or documents that are relevant to your application.
- we'll learn to build this all using langgraph's features for parallelization and human review.

### My Approach

(my approach is different in learning courses and write everything I need to understand it right and will take it slow - step by step - 1% better everyday)

- Go to **LangchainAcademyLangGraph** folder for more.

- Also updating every resource with latest version 3 URL.
