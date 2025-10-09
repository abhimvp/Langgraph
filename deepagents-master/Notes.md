# Deep Agents with LangGraph Notes

- [LearningFrom](https://github.com/langchain-ai/deepagents)
- Get Google API Key from [AiStudio](https://aistudio.google.com/app/api-keys).
- [Tavily API KEY](https://app.tavily.com/home) - Tavily Search API is a search engine optimized for LLMs, aimed at efficient, quick, and persistent search results
  - We'll use Tavily for building research agents with external search.
- Sign up & Get langsmith API KEY & reference its [documentation](https://docs.langchain.com/langsmith/home)
- Set environment variables: Create a .env file in the project root directory:

```.env
# Required for research agents with external search
TAVILY_API_KEY=your_tavily_api_key_here

# Required for model usage
# ANTHROPIC_API_KEY=your_anthropic_api_key_here
# OPENAI_API_KEY=your_openai_api_key_here
# I will be using GEMINI LLMs
GOOGLE_API_KEY=your_google_api_key_here

# Optional: For evaluation and tracing
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=deep-agents-from-scratch
```

- Install the package and dependencies - `uv sync` - This automatically creates and manages the virtual environment
- Activate the virtual environment - Windows - `source ./.venv/Scripts/activate`
- Read this on How [Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) has gained significant attention and popularity for long-horizon tasks: the average Manus task uses 50 tool calls!!!
- Careful review of the context engineering patterns across these popular "deep" agents shows some common approaches:

  - Task planning (e.g., todo), often with recitation
  - Context offloading to file systems
  - Context isolation through sub-agent delegation

- Refer offline notes for module - 1

  - 4 principles to keep in mind while building agents:
    - Planning
    - Offload context
    - Task Delegation
    - prompt engineering

- We'll be using the set of notebooks located [here](https://github.com/langchain-ai/deep-agents-from-scratch.git). Each module will also include links to the corresponding notebooks.
- i will be working on this `deep-agents-from-scratch-main` directory.
