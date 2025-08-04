from flask import Flask, session, request, render_template, jsonify
import openai
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
API_KEY = os.getenv('SESAC_API_KEY')
openai.api_key = API_KEY

client = openai.OpenAI(api_key=API_KEY)

def ask_chatgpt(user_input:str, history:list):
    gpt_question = {"role":"user", "content": user_input}
    history.append(gpt_question)
    
    # print('실제 전송되는 대화:', history)

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=history
    )

    gpt_response = {"role":"assistant", "content":response.choices[0].message.content}
    print(gpt_response)
    history.append(gpt_response)

    return gpt_response

@app.route('/')
def index():
    session['history'] = []
    return render_template('index.html')

@app.route('/question', methods=['POST'])
def question():
    user_input = request.form.get('userInput')
    
    history = session.get('history')
    gpt_res = ask_chatgpt(user_input, history)
        
    session['history'] = history

    return jsonify(gpt_res)


if __name__ == '__main__':
    app.run(debug=True)