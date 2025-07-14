from flask import Flask, send_file
from common import create_table
from api_route import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return send_file('static/todo.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)