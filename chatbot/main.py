from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


prompt = ChatPromptTemplate.from_messages([
    ('system','you are the best assistant in the world'),
    ('user','questions:{Questions}')
])

llm = ChatGroq(model='llama-3.3-70b-versatile', temperature=0.2)
parsers = StrOutputParser()

chain = prompt | llm | parsers

st.title('Testing the basic chatbot')
input_text = st.text_input('Enter your question here')

if input_text:
    st.write(chain.invoke({'Questions': input_text}))