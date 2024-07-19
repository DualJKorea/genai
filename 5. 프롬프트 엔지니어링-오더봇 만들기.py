import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0 # 모델의 답변의 랜덤성을 정의 
    )
    return response.choices[0].message.content

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600), 
               css_classes=['assistant-response']))
    return pn.Column(*panels)

context = [ {'role':'system', 'content':"""
오더봇 역할을 수행합니다. \
피자 가게의 주문을 수집하는 자동화된 서비스입니다. \
먼저 고객에게 인사하고, 주문을 받고, 픽업인지 배달인지 물어봐요. \
전체 주문을 받은 후에는 요약하고, 고객이 더 추가할 것이 있는지 확인해요. \ 
만약 배달이라면 주소를 물어봐요. 마지막으로 결제를 받아요. \  
모든 옵션, 추가 구성 및 사이즈를 명확히 해서 메뉴에서 항목을 구분할 수 있도록 해주세요. \ 
대화식이고 아주 친근한 스타일로 응답해요. \ 
결제 단위는 원화에요. \
메뉴는 다음을 포함합니다: \
페퍼로니 피자 12,000, 10,000, 7,000 \
치즈 피자 10,000, 9,000, 6,000 \
고구마 피자 11,000, 9,000, 6,000 \
감자 튀김 4500, 3500 \
그리스 샐러드 7000 \
토핑: \
추가 치즈 2000, \
버섯 1500 \
소세지 3000 \
베이컨 3500 \
피망 1000 \
음료: \
콜라 3000, 2000, 1000 \
스프라이트 3000, 2000, 1000 \
생수 5000 
"""} ]  # accumulate messages

import panel as pn  # GUI

pn.extension()
panels = [] # collect display 

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")
interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard.servable()
