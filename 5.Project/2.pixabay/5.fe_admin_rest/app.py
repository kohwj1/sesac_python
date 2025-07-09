from flask import Flask, request, url_for, jsonify, send_from_directory, redirect
import os
import csv

app = Flask(__name__)

images = [
    {'filename':'dog1.jpeg','keyword':['dog','animal','cute']},
    {'filename':'dog2.jpeg','keyword':['dog','animal','cute']},
    {'filename':'dog3.jpeg','keyword':['dog','animal','cute']},
    {'filename':'dog4.jpeg','keyword':['pet','animal','cute']},
    {'filename':'dog5.jpeg','keyword':['cat','animal']},
    {'filename':'cat1.jpeg','keyword':['cat','animal','cute']},
    {'filename':'cat2.jpeg','keyword':['cat','animal','cute']},
    {'filename':'cat3.jpeg','keyword':['cat','animal','cute']}
]

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/admin')
def admin():
    return send_from_directory(app.static_folder, 'admin.html')

@app.route('/api/search')
def search():
    q = request.args.get('q', '').lower()
    results = [url_for('static', filename=f"img/{item['filename']}") for item in images if q in item['keyword']]
    return jsonify({'url':results})

@app.route('/api/upload')
def upload():
    q = request.form.get()
    results = [url_for('static', filename=f"img/{item['filename']}") for item in images if q in item['keyword']]
    return jsonify({'url':results})

@app.route('/api/update_keyword')
def update_keyword():
    print('키워드 업뎃')
    return redirect(url_for('admin'))

@app.route('/api/delete/<filename>')
def delete(filename):
    print(f'이미지 삭제: {filename}')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    print('current server: fe_admin_template')
    app.run(debug=True)
