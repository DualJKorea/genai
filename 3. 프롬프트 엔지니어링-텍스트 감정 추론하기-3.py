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


lamp_review = """
침실용으로 좋은 램프가 필요했고, 이 제품은 추가 수납 공간이 있으면서도 가격이 너무 비싸지 않았습니다.\
빨리 받았어요. 램프의 스트링이 운송 중에 끊어졌는데, 회사가 기꺼이 새로운 것을 보내주었습니다. \
몇 일 안에 도착했습니다. 조립하기 쉬웠어요. 부품이 빠져 있었는데, 그들의 지원팀에 연락하여 빠르게 부품을 받았습니다! \
Lumina는 고객과 제품을 소중히 여기는 훌륭한 회사로 보입니다!!
"""

prompt = f"""
글쓴이의 리뷰에 분노가 표현되어있는지 추론하시오.
답변은 예 혹은 아니오로 답변할 것. 
리뷰 문구: '''{lamp_review}'''
"""

response = get_completion(prompt)
print(response)

