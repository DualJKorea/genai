import streamlit as st
from langchain_openai import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_response(txt):
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    text_splitter = CharacterTextSplitter()
    docs = [Document(page_content=t) for t in text_splitter.split_text(txt)]
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)

def translate_to_korean(response):
    prompt = PromptTemplate(input_variables=['input'], template='{input}를 한국어로 번역해 주세요')
    chain = LLMChain(llm=OpenAI(temperature=0, openai_api_key=openai_api_key), prompt=prompt)
    return chain.run(input=response)

st.set_page_config(page_title='텍스트 요약 앱')
st.title('텍스트 요약 앱')

txt_input = st.text_area('텍스트를 입력하세요', '', height=200)

with st.form('summarize_form', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not txt_input)
    submitted = st.form_submit_button('Submit')
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('작업 중...'):
            response = generate_response(txt_input)
            translated_response = translate_to_korean(response)
            st.info(translated_response)