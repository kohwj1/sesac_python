from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

@admin_bp.route('/')
def admin_page():
    return render_template('admin.html')