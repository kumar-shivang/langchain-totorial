from langchain_community.tools import TavilySearchResults
from langgraph.graph import END
from os import getenv
from dotenv import load_dotenv
from langchain_core.messages import ToolMessage
from graph import State
import json

load_dotenv()


class BasicToolsNode:
    def __init__(self, tools: list) -> None:
        self.tools_by_name = {tool.name: tool for tool in tools}
        # print(self.tools_by_name)

    def __call__(self, inputs: dict) -> dict:
        if messages := inputs.get("messages", []):
            message = messages[-1]
        else:
            raise ValueError("No message found in memory")
        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tools_by_name[tool_call["name"]].invoke(
                tool_call["args"]
            )  # go through all tool calls, and invoke them one by one using args
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
        return {"messages": outputs}


def route_tools(state: State):
    # NOTE: To be used in conditional edge in the graph
    """
    Conditionally route to the tool node if the last message has a tool call,
    otherwise route to the end.
    """
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get("messages", []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge:{state}")
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"
    return END


search = [TavilySearchResults()]

tool_node = BasicToolsNode(search)
