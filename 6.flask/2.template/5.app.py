from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name':'Alice', 'age':25, 'mobile':'0**-12**-5**8'},
    {'name':'Bob', 'age':30, 'mobile':'0**-11**-0**0'},
    {'name':'Charlie', 'age':35, 'mobile':'0**-12**-9**9'},
]

#이름/나이로 검색하기
@app.route('/')
def user_search():
    name = request.args.get('username')
    age = request.args.get('age')
    print(name, age)

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