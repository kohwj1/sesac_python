from flask import Flask, request, jsonify, send_file
from common import add_todo, delete_todo, get_all_list, switch_todo
from api_route import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return send_file('static/todo.html')

if __name__ == '__main__':
    app.run(debug=True)