from flask import Flask, send_file, redirect, request
from route.users_route import user_bp
from route.orders_route import order_bp
from route.stores_route import store_bp
from route.orderitems_route import orderitem_bp
from route.items_route import item_bp


app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order_bp, url_prefix='/api/orders')
app.register_blueprint(store_bp, url_prefix='/api/stores')
app.register_blueprint(item_bp, url_prefix='/api/items')
app.register_blueprint(orderitem_bp, url_prefix='/api/orderitems')

@app.route('/')
def index():
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True, port=5500)