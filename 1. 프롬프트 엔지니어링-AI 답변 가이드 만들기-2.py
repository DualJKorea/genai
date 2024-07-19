import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0 # 모델의 답변의 랜덤성을 정의 
    )
    return response.choices[0].message.content


prompt = f"""
책 제목과 작자, 장르로 구성된 목록을 한글로 만드시오.
JSON 포맷으로 만들고 키는 book_id, title, author, genre로 구성됩니다. 
"""

response = get_completion(prompt)
print('응답 : ',response)
