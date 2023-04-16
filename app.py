import streamlit as st
import openai
import os
from function import summarize

try:
    openai.api_key = os.getenv('OPENAI_KEY')
    
    if "like" not in st.session_state:
        st.session_state["like"] = ""
    
    st.title("Authorizer")
    
    input_text = st.text_area(label="Enter the name of poet or author and the genre:", value="", height=10)
    st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )
    output_text = st.text_area(label="Generated Text:", value=st.session_state["like"], height=250)
except:
    st.write('There was an error =(')