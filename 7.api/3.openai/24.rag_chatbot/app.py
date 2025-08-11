from flask import Flask, request, jsonify
import os
from vectorstore import init_vector_db, create_vector_db, answer_question, VECTOR_DB

app = Flask(__name__, static_url_path='')
DATA_DIR = 'DATA'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    if not file.filename:
        return jsonify({'msg':'파일이 존재하지 않습니다.'}), 400
    
    file_path = os.path.join(DATA_DIR, file.filename)
    file.save(file_path)

    create_vector_db(file_path)

    return jsonify({'msg':'업로드 성공'}), 200


@app.route('/ask', methods=['POST'])
def chatbot():
    data = request.get_json()
    q = data.get('q', '')
    answer = answer_question(q)   
    return jsonify({'msg':answer})


if __name__ == '__main__':
    app.run(debug=True)