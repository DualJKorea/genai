# pip install chromadb

import streamlit as st
from langchain_community.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

def generate_response(uploaded_file, openai_api_key, query_text):
    documents = [uploaded_file.read().decode()]
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.create_documents(documents)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = Chroma.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=openai_api_key), chain_type='stuff', retriever=retriever)
    return qa.run(query_text)

st.set_page_config(page_title='문서 기반 RAG 앱')
st.title('문서 기반 RAG 앱')

uploaded_file = st.file_uploader('문서를 업로드하세요', type='txt')
query_text = st.text_input('질문을 입력하세요:', placeholder='간단한 요약을 제공해 주세요.', disabled=not uploaded_file)

result = []
with st.form('myform', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text))
    submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and query_text))
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('작업 중...'):
            response = generate_response(uploaded_file, openai_api_key, query_text)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response)