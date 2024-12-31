from langchain_core.messages import HumanMessage

from app import graph
import streamlit as st


st.title("Langchain Tutorial")

input_text = st.text_input("write something")
stream = st.checkbox("Stream text")
if input_text:
    if stream:
        # BUG:- It's not working as expected, would fix it later
        st.write_stream(graph.stream({"messages": [("user", input_text)]}))
    else:
        st.write(
            graph.invoke({"messages": [("user", input_text)]})["messages"][-1].content
        )
