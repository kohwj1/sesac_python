from flask import Flask, jsonify, render_template

app = Flask(__name__)

users = [
    {'name':'Alice', 'age':25, 'mobile':'0**-12**-5**8'},
    {'name':'Bob', 'age':30, 'mobile':'0**-11**-0**0'},
    {'name':'Charlie', 'age':35, 'mobile':'0**-12**-9**9'},
]

@app.route('/')
def home():
    return render_template('index3.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)