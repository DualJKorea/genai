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


text_1 = f"""
차 한 잔 만드는 것은 쉽습니다! 먼저 물을 끓이세요. \
그 동안 컵을 가져와 그 안에 차를 담으세요. 물이 충분히 뜨거워지면, \
그냥 차를 티백 위에 따르세요. 차가 우러나올 수 있도록 잠깐 기다려주세요. \
몇 분 후에 티백을 빼내세요. 원한다면 설탕이나 우유를 넣어 맛을 조절할 수 있습니다. \
그럼 끝났어요! 맛있는 차 한 잔이 완성되었습니다.
"""

prompt = f"""
삼중 쿼테이션으로 감싸진 문장이 있습니다. 
만약 문장 구조가 순서가 있으면, 다음과 같이 한글로 정리하시오.

스텝 1 - ...
스텝 2 - ...
...
스텝 N - ...
문장 구조에 순서가 없으면 \"순서가 없음\" 이라고 적으시오.

\"\"\"{text_1}\"\"\"
"""

response = get_completion(prompt)
print('응답 : ',response)
