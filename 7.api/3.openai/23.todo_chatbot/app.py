from dotenv import load_dotenv
from flask import Flask, request, jsonify, blueprints
from routes.todo import todo_bp
from routes.chat import chat_bp

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path="")
app.register_blueprint(todo_bp, url_prefix='/api/todo')
app.register_blueprint(chat_bp, url_prefix='/api/chat')

todos = []

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)