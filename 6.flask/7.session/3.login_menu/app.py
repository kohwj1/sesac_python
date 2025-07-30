from flask import Flask, request, render_template, session, redirect, url_for
# from flask_session import Session

users = [
    {'name':'홍길동', 'id':'user1', 'pw':'test'}
]

cart = []

items = [
    {'id':'prod-01', 'name':'사과', 'price':1000},
    {'id':'prod-02', 'name':'딸기', 'price':2000},
    {'id':'prod-03', 'name':'바나나', 'price':2500}
]

app = Flask(__name__)
app.secret_key = 'mymy-test-key'

@app.route('/')
def home():
    current_user = session.get('user', None)
    return render_template('index.html', isSigned=current_user)

@app.route('/user')
def user():
    current_user = session.get('user', None)

    if current_user:
        return render_template('user.html', name=current_user['name'], isSigned=current_user)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userid = request.form.get('id', None)
        userpw = request.form.get('pw', None)
    
        user = next((u for u in users if u['id'] == userid and u['pw'] == userpw), None)

        if user:
            session['user'] = user
            session['cart'] = {}
            return redirect(url_for('user'))
        else:
            return render_template('login.html', error='아이디 또는 비밀번호가 잘못되었습니다?')

    else:
        if session.get('user'):
            return redirect(url_for('user'))
    return render_template('login.html', error='')

@app.route('/product')
def product():
    current_user = session.get('user', None)
    return render_template('product.html', items=items, isSigned=current_user)

@app.route('/add-to-cart', methods=['POST'])
def add_cart():
    current_user = session.get('user')

    if current_user:
        pid = request.form.get('pid')
        mycart = session['cart']

        if pid in mycart:
            mycart[pid] += 1
        else:
            mycart[pid] = 1
        
        session['cart'] = mycart

        print(session['cart'])
        return render_template('product.html', items=items, isSigned=current_user)

    else:
        return render_template('product.html', items=items, isSigned=False, error='로그인 후 이용 가능합니다.')

@app.route('/cart')
def mycart():
    current_user = session.get('user', None)
    cart_data = session.get('cart', {})
    mycart = []

    for item_id, item_qantity in cart_data.items():
        item = next((i for i in items if i['id'] == item_id), None)
        if item:
            a_item = item.copy()
            a_item['quantity'] = item_qantity
            mycart.append(a_item)

    return render_template('cart.html', mycart=mycart, isSigned=current_user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('cart', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)