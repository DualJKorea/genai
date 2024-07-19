
import streamlit as st
from langchain.llms import OpenAI

st.title('대화형 챗봇 샘플')

openai_api_key = st.sidebar.text_input('OpenAI API 키')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('myform'):
  text = st.text_area('질문를 입력하세요:')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 키를 입력하세요', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)


