from flask import Flask, redirect
from route.users_route import user_bp
from route.orders_route import order_bp
from route.stores_route import store_bp
from route.orderitems_route import orderitem_bp
from route.items_route import item_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order_bp, url_prefix='/orders')
app.register_blueprint(store_bp, url_prefix='/stores')
app.register_blueprint(item_bp, url_prefix='/items')
app.register_blueprint(orderitem_bp, url_prefix='/orderitems')

@app.route('/')
def index():
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)




