from app import graph
import streamlit as st


st.title("Langchain Tutorial")

input_text = st.text_input("write something")
stream = st.checkbox("Stream text")
if input_text:
    if stream:
        # FIX:- It's not working as expected, would fix it later
        st.write_stream(graph.stream({"messages": [("user", input_text)]}))
    else:
        output = graph.invoke({"messages": [("user", input_text)]})["messages"][-1]
        st.write(output.content)
        # FIX: find a way to check output tool_calls
        print(output.tool_calls)
