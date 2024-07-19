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


prod_review = """
내 딸의 생일을 위해 이 판다 인형을 샀는데, \
딸 애는 그것을 정말 좋아해서 어디든지 가져다닌다. \
부드럽고 너무 귀여워서, 얼굴도 친근한 느낌이다. \
하지만 내가 지불한 가격에 비해 조금 작은 편이다. \
같은 가격으로 더 큰 옵션이 있을 것 같아서 아쉽다. \
예상보다 하루 일찍 도착해서, 좋았다. 
"""

prompt = f"""
이커머스 사이트에 개시된 상품 리뷰를 간단하게 요약할 것. 
백슬래시로 구분된 리뷰를 한글로 요약할 것. 
리뷰 : ```{prod_review}```
""" 

response = get_completion(prompt)
print(response)


