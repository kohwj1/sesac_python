from flask import Flask, jsonify, send_from_directory, request
from dotenv import load_dotenv
import openai, os, time

load_dotenv()

API_KEY = os.getenv('SESAC_API_KEY')
client = openai.OpenAI(api_key=API_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    userInput = data['userInput']
    time.sleep(2)
    gpt_answer = ask_gpt(userInput)
    return jsonify({'response': gpt_answer})

history = []

def ask_gpt(user_input):
    history.append({'role':'user', 'content':user_input})
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=history,
        temperature=0.8
    )
    answer = response.choices[0].message.content

    history.append({'role':'assistant', 'content':answer})

    # if len(history) > 10:
    #     history = history[2:]
    #     print(history)
    #     print(f'대화 내용 길이: {len(history)}')

    return answer

if __name__ == '__main__':
    app.run(debug=True)