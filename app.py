import os
from typing import Annotated

import streamlit as st
from dotenv import load_dotenv

# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

load_dotenv()


model = ChatMistralAI(
    model_name="mistral-medium", api_key=os.getenv("MISTRALAI_API_KEY")
)

st.title("Langchain")
st.write(model.invoke("Hi").content)
