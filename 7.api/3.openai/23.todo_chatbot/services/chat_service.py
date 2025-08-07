from dotenv import load_dotenv
from openai import OpenAI
from services import todo_service as todo
import json

load_dotenv()
client = OpenAI()
my_todo_list = todo.get_all()

def request_to_bot(userInput):
    # system_template = f"""
    #     당신은 사용자의 TODO 리스트를 관리해주는 비서입니다. 사용자의 TODO 항목과 질문에 대해 간결하게 답변해주세요.

    #     [할 일 목록]
    #     {my_todo_list}
    #     """
    system_template = f"""
        당신은 사용자의 TODO 리스트를 관리해주는 비서입니다.
        사용자의 질문에 대해서 아래 중 하나를 골라 action을 선택하고 답변해야 합니다.
        사용자의 todo 항목과 질문에 대해서 간결하게 답변해 주세요.

        [출력 형식]
        {{"action":"add", "item":[항목]]}} - todo 목록에 할 일을 추가할 때
        {{"action":"toggle", "item":[항목]}} - todo 목록 중 특정 할 일을 완료했거나, 완료한 일을 다시 미완료 상태로 바꿀 때
        {{"action":"delete", "item":[항목]}} - todo 목록에서 할 일을 삭제할 때
        {{"action":"list"}} - todo 목록을 보여줘야 할 때
        {{"action":"none"}} - 그 외 todo와 관련 없는 질문이 들어왔을 떄
        """
    
    prompt_history = [
                {"role":"system", "content":system_template},
                {"role":"user", "content":userInput},
            ]

    res = client.chat.completions.create(
        messages=prompt_history,
        model='gpt-3.5-turbo'
    )
    bot_response = json.loads(res.choices[0].message.content.strip())

    if bot_response['action'] == 'list':
        answer = bot_list()

    elif bot_response['action'] == 'add':
        answer = bot_add(bot_response['item'])

    elif bot_response['action'] == 'toggle':
        answer = bot_toggle(bot_response['item'])

    elif bot_response['action'] == 'delete':
        answer = bot_delete(bot_response['item'])
    else:
        answer = bot_common_chat(userInput)
    return answer

def bot_list():
    todo_ready_list = [f"- {item.get('task')}" for item in my_todo_list if not item.get('is_done')]

    if not todo_ready_list:
        return "오늘 할일이 없거나 모두 완료한 상태입니다. 여유로운 날이군요!"

    answer = "오늘의 할일 목록입니다.\n"
    answer += '\n'.join(todo_ready_list)

    return answer

def bot_add(item):
    todo.add(item)
    answer = f"할일 목록에 {item}을 추가하였습니다."
    return answer

def bot_toggle(item):
    print(item)
    status = '미완료'

    for i, task in enumerate(my_todo_list):
        if task['task'] == item:
            print(i)
            res = todo.toggle(i)
            if res.get('is_done'):
                status = '완료'
            return f'{item}의 할일 상태를 {status}로 변경했습니다.'
    
    return f'{item}이 할일 목록에 없습니다. 다시 한번 확인해주세요.'

def bot_delete(item):
    for i, task in enumerate(my_todo_list):
        if task['task'] == item:
            todo.delete(i)
            return f'{item}을 할일 목록에서 삭제하였습니다.'
    
    return f'{item}이 할일 목록에 없습니다. 다시 한번 확인해주세요.'

def bot_common_chat(userInput):
    prompt_history = [
                {"role":"user", "content":userInput},
    ]

    res = client.chat.completions.create(
        messages=prompt_history,
        model='gpt-3.5-turbo',
        temperature=0.8
    )
    return res.choices[0].message.content.strip()