from flask import Flask, request, jsonify
import os
from vectorstore import initialize_vector_db, create_vector_db, delete_file_from_vstore
from chatbot import initialize_llm, answer_question

app = Flask(__name__, static_url_path="")

DATA_DIR = "DATA"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "파일이 없습니다."})
    
    file = request.files['file']
    if file:
        file_path = os.path.join(DATA_DIR, file.filename)
        file.save(file_path)
    
    # 받아온 문서를 백터DB에 추가한다..
    result = create_vector_db(file_path)
    if result:
        return jsonify({"message": "파일이 성공적으로 업로드 되었습니다."})        
    else:
         return jsonify({"message": "파일은 업로드 되었으나, DB가 정상적으로 생성되지 못했습니다."})    

@app.route('/ask', methods=['POST'])
def chatbot():
    data = request.get_json()
    question= data.get('question', '')
    
    answer = answer_question(question)
    
    return jsonify({"message": answer})

@app.route('/files')
def get_filelist():
    files = [f for f in os.listdir(DATA_DIR)
             if os.path.isfile(os.path.join(DATA_DIR, f))]
    return jsonify({"files": files})

@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    # 벡터DB에서 삭제
    delete_file_from_vstore(filename)
    
    # 물리적으로 파일 삭제
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        
    return jsonify({"message": f"'{filename}' 을 삭제하였습니다."})

if __name__== "__main__":
    initialize_vector_db()
    initialize_llm()
    app.run(debug=True)