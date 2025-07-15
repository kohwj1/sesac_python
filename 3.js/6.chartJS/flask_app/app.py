from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    data = {
        'labels':['1월','2월','3월','4월','5월','6월','7월'],
        'values':[100, 90, 80, 70, 60, 50, 40]
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)