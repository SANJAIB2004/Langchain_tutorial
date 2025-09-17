from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI
import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


app = FastAPI(
    title="LangChain Groq Chatbot API",
    description="An API for a chatbot using LangChain and Groq",
)


groq_model = ChatGroq(model='llama-3.3-70b-versatile', temperature=0.2)

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    groq_model,
    path = '/groq'
)

add_routes(
    app,
    prompt1|groq_model,
    path = '/essay'
)

add_routes(
    app,
    prompt2|groq_model,
    path = '/poem'
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)