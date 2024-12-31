import os

import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from graph import graph_builder

load_dotenv()


model = ChatMistralAI(
    model_name="mistral-medium", api_key=os.getenv("MISTRALAI_API_KEY")
)

graph_builder.add_node("model", model)  # adding the model to the graph
graph_builder.add_edge(START, "model")

graph = graph_builder.compile()

with open("graph.txt", "w") as file:
    file.write(graph.get_graph().draw_ascii())


st.title("Langchain")
st.write("placeholder text")
