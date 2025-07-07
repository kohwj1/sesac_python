from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name':'Alice', 'age':25, 'mobile':'0**-12**-5**8'},
    {'name':'Bob', 'age':30, 'mobile':'0**-11**-0**0'},
    {'name':'Charlie', 'age':35, 'mobile':'0**-12**-9**9'},
]

@app.route('/')
def index():
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):
    user = None
    # try:
    # age = int(name)
    # for u in users:
    #     if u['age'] == age:
    #         user = u
    #         break
    # except ValueError:
    for u in users:
        if u['name'].lower() == name.lower():
            user = u
            break
    if user:
        return jsonify(user)
    return jsonify({'status':'fail','message':'user not found'}), 404

@app.route('/user/<int:age>')
def geet_user_by_age(age):
    user = None
    for u in users:
        if u['age'] == age:
            user = u
            break
    if user:
        return jsonify(user)
    return jsonify({'status':'fail','message':'user not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)