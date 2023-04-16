import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"generate text like given author and genre: {prompt}"
    try:
        st.session_state["like"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')