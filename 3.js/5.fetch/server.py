from flask import Flask, send_file, jsonify
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    return send_file('4.fetch.html')

@app.route('/data')
def data():
    return jsonify({'result':1, 'message':'안녕하세요, 반갑습니다!'})

if __name__ == '__main__':
    app.run(debug=True)