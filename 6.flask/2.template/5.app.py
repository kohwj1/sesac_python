from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name':'Alice', 'age':25, 'mobile':'050-1111-1111'},
    {'name':'Alice', 'age':35, 'mobile':'050-5555-5555'},
    {'name':'Bob', 'age':30, 'mobile':'050-2222-2222'},
    {'name':'Charlie', 'age':35, 'mobile':'050-3333-3333'},
    {'name':'Charlie', 'age':30, 'mobile':'050-4444-4444'}
]

#이름/나이로 검색하기
@app.route('/')
def user_search():
    name = request.args.get('username')
    age = request.args.get('age')
    result = users

    if name and age:
        result = [u for u in users if (u['name'].lower() == name.lower()) and (u['age'] == int(age))]
    elif name:
        result = [u for u in users if (u['name'].lower() == name.lower())]
    elif age:
        result = [u for u in users if (u['age'] == int(age))]
    
    return render_template('index5.html', users=result)

if __name__ == '__main__':
    app.run(debug=True)