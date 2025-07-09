from flask import Flask, request, render_template, url_for, jsonify
import random

app = Flask(__name__)

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
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q', '').lower()
    results = [url_for('static', filename=f"img/{item['filename']}") for item in images if q in item['keyword']]
    # for item in images:
    #     if any(q in keyword for keyword in item['keyword']):
    #         image_url = url_for('static', filename=f"img/{item['filename']}")
    #         results.append(image_url)

    return render_template('results.html', q=q, results=results)

if __name__ == '__main__':
    app.run(debug=True)
