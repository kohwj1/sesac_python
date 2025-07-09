from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, template_folder='../templates/user') #용도별로 파일을 분리하면서 경로가 달라졌으므로 기본 경로를 변경해야

@user_bp.route('/')
def user_page():
    return render_template('user.html')