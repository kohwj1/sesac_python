from flask import Flask, request, render_template, url_for, redirect
import os, json

app = Flask(__name__)
UPLOAD_FOLDER = 'static/img'
allowed_EXET = {'jpg', 'png',' jpeg'}


def get_images():
    images = []
    for file in os.listdir(UPLOAD_FOLDER):
        print(file)
        if file.endswith('.jpeg') or file.endswith('.jpg'):
            # images.append({'filename':file, 'keyword':['dog','animal','cute']})
            images.append({'filename':file, 'keyword':['dog','animal','cute']})
    return images

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', images=get_images())

@app.route('/search')
def search():
    q = request.args.get('q', '').lower()
    results = [url_for('static', filename=f"img/{item['filename']}") for item in get_images() if q in item['keyword']]
    return render_template('results.html', q=q, results=results)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    #업로드 시 파일 선택 여부는 프론트의 input에 required 속성으로 대체
    file_path = os.path.join('./', UPLOAD_FOLDER, file.filename.replace(' ','_'))
    file.save(file_path)
    return redirect(url_for('admin'))

@app.route('/update_keyword/<filename>', methods=['POST'])
def update_keyword(filename):
    new_keyword = request.form.get('newKeyword')
    print(f'{filename}의 키워드를 {new_keyword}로 업데이트')
    return redirect(url_for('admin'))

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    file_path = os.path.join('./', UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
    except FileNotFoundError:
        return '파일이 존재하지 않거나 이미 삭제되었습니다.'
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
