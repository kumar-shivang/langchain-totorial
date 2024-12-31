from tools import tool_node, route_tools
from graph import State, graph_builder
from langgraph.graph import END, START
from langchain_mistralai import ChatMistralAI
from tools import search
import os

from dotenv import load_dotenv

load_dotenv()

llm = ChatMistralAI(
    model_name="mistral-large-2407", api_key=os.getenv("MISTRALAI_API_KEY")
)

llm = llm.bind_tools(search)


def model(state: State):  # for testing
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("model", model)  # adding the model to the graph
graph_builder.add_node("tools", tool_node)
graph_builder.add_edge(START, "model")
graph_builder.add_conditional_edges(
    "model",
    route_tools,
    {
        "tools": "tools",  # NOTE: if route_tools return tools...go to tool_node
        END: END,  # NOTE: if route_tools return END, go to the END node
    },
)
graph_builder.add_edge("tools", "model")
# graph_builder.set_entry_point("model")
# graph_builder.set_finish_point("model")
graph = graph_builder.compile()

with open("graph.txt", "w") as file:
    file.write(graph.get_graph().draw_ascii())
