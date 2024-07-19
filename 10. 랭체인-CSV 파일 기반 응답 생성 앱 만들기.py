# pip install langchain_experimental
# pip install tabulate

import streamlit as st
import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType

st.set_page_config(page_title='CSV 파일 기반 응답 생성 앱')
st.title('CSV 파일 기반 응답 생성 앱')

def load_csv(file):
    df = pd.read_csv(file, encoding='cp949')
    with st.expander('데이터프레임 보기'):
        st.write(df)
    return df

def generate_response(csv_file, query, api_key):
    llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key=api_key)
    df = load_csv(csv_file)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
    response = agent.run(query)
    return st.success(response)

uploaded_file = st.file_uploader('CSV 파일을 업로드 하세요', type=['csv'])
question_list = [
    '업로드한 CSV 파일에 행(Row)이 몇 개 있나요?',
    '업로드한 CSV 파일에 칼럼(Column)이 몇 개 있나요?',
    '기타'
]
selected_question = st.selectbox('예시 질문을 선택하세요:', question_list, disabled=not uploaded_file)
api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and selected_question))

if selected_question == '기타':
    query_text = st.text_input('질문을 입력하세요:', placeholder='여기에 질문을 입력하세요...', disabled=not uploaded_file)
else:
    query_text = selected_question

if not api_key.startswith('sk-'):
    st.warning('유효한 OpenAI API 키를 입력하세요', icon='⚠')
elif uploaded_file is not None and query_text:
    st.header('결과')
    generate_response(uploaded_file, query_text, api_key)

