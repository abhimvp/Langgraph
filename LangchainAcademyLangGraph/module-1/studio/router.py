import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
google_api_key = os.environ.get("GOOGLE_API_KEY")

if google_api_key:
    print("Successfully loaded and retrieved the Google API key from the .env file.")
else:
    print("Could not find the 'GOOGLE_API_KEY' in the .env file or the environment.")


# Tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b


# LLM with bound tool
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)
llm_with_tools = llm.bind_tools([multiply])


# Node
def tool_calling_llm(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


# Build graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([multiply]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", END)

# Compile graph
graph = builder.compile()
