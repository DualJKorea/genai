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
너의 임무는 상황극의 대답을 하는거야. 
<아이>: 인내심을 가르쳐 주세요.
<할머니>: 
가장 깊은 곳을 깎는 강과 계곡은 완만한 샘에서 시작되어 흐른단다.
가장 웅장한 교향곡은 한 음에서 비롯되고,
가장 복잡한 태피스트리도 하나의 실에서 시작되는 거야.
<아이>: 회복에 대해 가르쳐 주세요.  
"""

response = get_completion(prompt)
print('응답 : ',response)
