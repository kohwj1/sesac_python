from flask import Flask, request, url_for, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

images = [
    {'filename':'dog1.jpeg','keyword':['dog','animal','cute']},
    {'filename':'dog2.jpeg','keyword':['dog','animal','cute']},
    {'filename':'dog3.jpeg','keyword':['dog','animal','cute']},
    {'filename':'dog4.jpeg','keyword':['pet','animal','cute']},
    {'filename':'dog5.jpeg','keyword':['cat','animal']},
    {'filename':'cat1.jpeg','keyword':['cat','animal','cute']},
    {'filename':'cat2.jpeg','keyword':['cat','animal','cute']},
    {'filename':'cat3.jpeg','keyword':['cat','animal','cute']}
]

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/search')
def search():
    q = request.args.get('q', '').lower()
    results = [url_for('static', filename=f"img/{item['filename']}") for item in images if q in item['keyword']]
    return jsonify({'url':results})

if __name__ == '__main__':
    app.run(debug=True)
