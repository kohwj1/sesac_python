from flask import Flask, request, render_template, session, redirect, url_for, flash
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

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    current_user = session.get('user', None)

    if current_user:
        if request.method == 'POST':
            new_name = request.form.get('name')
            new_pw = request.form.get('pw')

            if new_name and new_pw:
                user = next((u for u in users if u['id'] == current_user['id']), None)
                user['name'] = new_name
                user['pw'] = new_pw
                session['user'] = user
                flash('정보가 업데이트되었습니다.') 
            else:
                return '비정상 접근입니다.'
        else:
            return render_template('profile.html', name=current_user['name'], isSigned=current_user)
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

@app.route('/product', methods=['POST'])
def add_cart():
    current_user = session.get('user')

    if current_user:
        pid = request.form.get('pid')
        mycart = session['cart'] #현재 카트정보 가져오기

        if pid in mycart:
            mycart[pid] += 1
        else:
            mycart[pid] = 1
        
        flash(f'장바구니에 {pid}을(를) 담았습니다')
        session['cart'] = mycart #변경된 카트정보로 세션 업데이트

        # print(session['cart'])
        return render_template('product.html', items=items, isSigned=current_user)

    else:
        return render_template('product.html', items=items, isSigned=False, error='로그인 후 이용 가능합니다.')

@app.route('/cart', methods=['POST', 'GET'])
def mycart():
    current_user = session.get('user', None)
    cart_data = session.get('cart', {})

    #장바구니 수량 변경
    if request.method == 'POST':
        mycart = session['cart']
        for pid in request.form.keys():
            # print(pid, request.form.get(pid))
            mycart[pid] = int(request.form.get(pid))
        
        session['cart'] = mycart
        flash('장바구니 상품 수량이 변경되었습니다')
        return redirect(url_for('mycart'))
    
    #장바구니 조회
    else:
        mycart = []

        for pid, q in cart_data.items():
            item = next((i for i in items if i['id'] == pid), None) #pid를 기준으로 매칭되는 아이템을 items에서 찾아옴
            if item:
                a_item = item.copy()
                a_item['q'] = q
                mycart.append(a_item)

        return render_template('cart.html', mycart=mycart, isSigned=current_user)
    
@app.route('/delete')
def delete_cart():
    current_user = session.get('user', None)
    pid = request.args.get('pid')

    if not current_user or not pid:
        return '잘못된 접근입니다.'

    mycart = session['cart']
    mycart.pop(pid)
    session['cart'] = mycart
    flash('장바구니에서 상품을 삭제하였습니다')
    return redirect(url_for('mycart'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('cart', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)