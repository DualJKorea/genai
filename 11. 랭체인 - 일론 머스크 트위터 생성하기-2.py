import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Importing verbose from langchain root module is no longer supported.")

import openai
import os 
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')

import langchain
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

normal_chain = (
    ChatPromptTemplate.from_messages([(
        "system","write a tweet about {topic} in the style of Elon Musk in korean")])
    | ChatOpenAI()
    | StrOutputParser()
)

chain = (
    ChatPromptTemplate.from_messages([(
        "system","write a tweet about {topic} in korean")])
    | ChatOpenAI(model="ft:gpt-3.5-turbo-0125:personal::xxxxxx")
    | StrOutputParser()
)

def generate_tweet_normal(topic):
    result = normal_chain.invoke({"topic": topic})
    return result

def generate_tweet(topic):
    result = chain.invoke({"topic": topic})
    return result

col1, col2 = st.columns([1, 6])   
col1.image("elon.jpeg")   

col2.title("Elon Musk Tweet Generator")
topic = st.text_input("Enter a topic:")

if st.button("Generate Tweets"):
    if topic:
        col3, col4 = st.columns([6, 6])
        tweet = generate_tweet(topic)
        col3.markdown("### Finetuned Tweet:")
        col3.write(f"🐦: {tweet}")        
        tweet = generate_tweet_normal(topic)
        col4.markdown("### Prompted Tweet:")
        col4.write(f"🐦: {tweet}")         
    else:
        st.warning("Please enter a topic before generating a tweet.")
