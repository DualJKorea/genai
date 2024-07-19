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

text = f"""
모델이 해야 할 일을 명확하고 구체적으로 설명하는 지침을 제공하여야 합니다 \ 
이는 모델을 원하는 결과물로 안내하고, 부적절하거나 잘못된 응답을 받을 가능성을 줄입니다 \
명료한 프롬프트를 작성하는 것과 짧은 프롬프트를 작성하는 것을 혼동하지 마세요 \
많은 경우, 더 긴 프롬프트가 모델에게 더 많은 명확성과 맥락을 제공하여 \
더 자세하고 관련성 높은 결과물을 도출할 수 있습니다
"""

prompt = f"""
백슬래시로 구분된 여러 문장을 2개 문장으로 요약하시오. 
```{text}```
"""

response = get_completion(prompt)
print('응답 : ',response)


