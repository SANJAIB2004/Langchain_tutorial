import requests
import streamlit as st 


def get_groq_api_essay(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_groq_api_poem(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

st.title('Creating the routes and adding it via FASTAPI')
input_text = st.text_input("write an essay on")
input_text2 = st.text_input("write a poem on")

if input_text:
    st.write(get_groq_api_essay(input_text))
if input_text2:
    st.write(get_groq_api_poem(input_text2))