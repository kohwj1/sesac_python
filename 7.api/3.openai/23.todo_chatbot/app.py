from dotenv import load_dotenv
from flask import Flask, request, jsonify, blueprints

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path="")

todos = []

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/todo', methods=['GET'])
def get_list():
    return jsonify({'msg':'error'})

@app.route('/api/todo', methods=['POST'])
def add_todo():
    return jsonify({'msg':'error'})

@app.route('/api/todo/<id>', methods=['PUT'])
def update_todo():
    return jsonify({'msg':'error'})

@app.route('/api/todo/<id>', methods=['DELETE'])
def delete_todo():
    return jsonify({'msg':'error'})


if __name__ == '__main__':
    app.run(debug=True)