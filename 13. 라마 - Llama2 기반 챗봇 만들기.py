from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the questions in korean"),
        ("user","Question:{question}")
    ]
)

st.title('Langchain Chatbot With LLAMA2 model')   
input_text=st.text_input("Ask your question!")   

llm=Ollama(model="llama2")

chain=prompt|llm

if input_text:
    st.write(chain.invoke({"question":input_text}))
