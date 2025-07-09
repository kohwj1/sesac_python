from flask import Blueprint, render_template

product_bp = Blueprint('product', __name__, template_folder='../templates/product')

@product_bp.route('/')
def product_page():
    return render_template('product.html')