import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Importing verbose from langchain root module is no longer supported.")

import openai
import os 
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')

import streamlit as st
from langchain.agents import Tool
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

wrapper = DuckDuckGoSearchAPIWrapper(time="d", max_results=2)
ddg_search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")

chain = (
    ChatPromptTemplate.from_messages([(
        "system","다음 뉴스를 요약해줘. {topic} ")])
    | ChatOpenAI()
    | StrOutputParser()
)

st.title("Internet News with AI")
topic = st.text_input("Enter a question:")

if st.button("Web Search and Summary"):
    if topic:
        search_result = ddg_search.run(topic)
        summ_result = chain.invoke({"topic": search_result})
        
        col3, col4 = st.columns([6, 6])
        col3.markdown("### Summarize:")
        col3.write(f"{summ_result}")        
        
        col4.markdown("### Internet Source:")
        col4.write(f"{search_result}")         
    else:
        st.warning("Please enter a question.")
        