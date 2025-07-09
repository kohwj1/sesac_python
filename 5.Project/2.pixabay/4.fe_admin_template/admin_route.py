from flask import Blueprint, render_template, request, redirect, url_for
from csvControl import UPLOAD_FOLDER, get_images, set_keywords, add_to_csv
import os

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def admin():
    return render_template('admin.html', images=get_images())

@admin_bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    replaced_filename = file.filename.replace(' ','_')
    #업로드 시 파일 선택 여부는 프론트 input의 required 속성으로 대체
    file_path = os.path.join('./', UPLOAD_FOLDER, replaced_filename)
    file.save(file_path)

    for item in get_images():
        if item['filename'] == replaced_filename:
            return redirect(url_for('admin.admin'))
    add_to_csv(replaced_filename)
    return redirect(url_for('admin.admin'))

@admin_bp.route('/update_keyword/<filename>', methods=['POST'])
def update_keyword(filename):
    new_keyword = request.form.get('newKeyword')
    # print(f'{filename}의 키워드를 {new_keyword}로 업데이트')
    set_keywords(filename, new_keyword)
    return redirect(url_for('admin.admin'))

@admin_bp.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    file_path = os.path.join('./', UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
    except FileNotFoundError:
        return '파일이 존재하지 않거나 이미 삭제되었습니다.'
    return redirect(url_for('admin.admin'))