
import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

st.set_page_config(page_title="문서 개요 생성 앱")
st.title('문서 개요 생성 앱')

openai_api_key = st.sidebar.text_input('OpenAI API 키', type='password')

def generate_response(topic):
  llm = OpenAI(model_name='gpt-3.5-turbo-instruct', openai_api_key=openai_api_key)
  template = '{topic} 키워드로 작성할 문서의 개요를 생성해 주세요.'
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  response = llm.invoke(prompt_query)
  return st.info(response)

with st.form('myform'):
  topic_text = st.text_input('키워드를 입력하세요:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 키를 입력하세요', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(topic_text)

