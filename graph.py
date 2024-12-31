from typing import Annotated
from langgraph.graph import StateGraph, add_messages
from typing_extensions import TypedDict


class State(TypedDict):
    """
    This is a dictionary that store the current state of the graph
    (or messages, not sure yet)
    """

    messages = Annotated[list, add_messages]
    # NOTE:: Updates to messages will be appended to the
    # existing list rather than overwriting it,
    # thanks to the prebuilt add_messages function
    # used with the Annotated syntax


# NOTE: Each node can receive the current State as input and output an update
# to the state.

graph_builder = StateGraph(State)
