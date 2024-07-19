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


fact_sheet_chair = """
소개 

- 아름다운 미드 센츄리 영감을 받은 사무용 가구 시리즈의 일부로, 파일 캐비닛, 책상, 책장, 회의 테이블 등이 포함됩니다.
- 쉘 색상과 베이스 마감의 여러 옵션이 있습니다.
- 플라스틱 등받이와 전면 패브릭을 사용할 수 있습니다 (SWC-100) 또는 10가지 패브릭 및 6가지 가죽 옵션으로 완전히 덮인 (SWC-110) 옵션으로 제공됩니다.
- 베이스 마감 옵션은 스테인레스 스틸, 무광 블랙, 광택 있는 화이트, 또는 크롬입니다.
- 의자에서 팔걸이 여부를 선택할 수 있습니다.
- 가정용 또는 비즈니스 환경에 적합합니다.
- 계약 사용에 적격입니다.

구조

- 5개의 플라스틱 코팅된 알루미늄 베이스.
- 편압식 의자 조절로 쉬운 높이 조절/내림 작업이 가능합니다.

크기

- 폭 53cm | 20.87인치
- 깊이 51cm | 20.08인치
- 높이 80cm | 31.50인치
- 좌석 높이 44cm | 17.32인치
- 좌석 깊이 41cm | 16.14인치

옵션

- 소프트 또는 하드 바닥 캐스터 옵션.
- 좌석 폼 밀도 두 가지 선택: 중간 (1.8 lb/ft3) 또는 고밀도 (2.8 lb/ft3)
- 팔걸이 없음 또는 8개의 위치로 조절 가능한 PU 팔걸이

소재

쉘 베이스 글라이더

- 수정된 나일론 PA6/PA66 코팅이 된 주조 알루미늄.
- 쉘 두께: 10mm.

좌석

- HD36 폼

원산지

- 이탈리아
"""

prompt = f"""
마케팅 팀 입장에서 상품의 제원 시트를 기반으로 웹사이트에 개시할 상품정보를 작성하시오.
상품의 설명은 주어진 기술 스펙 정보를 기반으로 작성되어야 함.
이 설명은 가구 소매업체를 대상으로 하므로 기술적이어야 하며, 
상품을 구성하는 재료의 설명에 중점을 두어야 함.
제품 상세에 끝부분에, 7자의 상품ID를 같이 표기할 것.
최대 50단어 이내로 한글로 작성하시오.
제품 상세: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print('응답 : ',response)
