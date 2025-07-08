from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True) #폴더 생성 (있어도 허용)

def get_filelist():
    filelist = os.listdir(UPLOAD_FOLDER)
    return filelist

def get_filesize(file):
    pos = file.stream.tell() #현재 포인터 기록
    file.stream.seek(0, os.SEEK_END) #포인터 끝까지 이동 (용량 측정)
    size = file.stream.tell() #끝자리 (=파일 용량)을 사이즈로 기록
    file.stream.seek(pos) #사이즈 확인 후 포인터 초기화
    return size

def allowed_file(filename:str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT

@app.route('/')
def index():
    return render_template('upload12.html', filelist=get_filelist())

@app.route('/upload', methods=['POST'])
def upload_file():
    #file = request.form    # 속성, 파일명만 받아옴
    print(request.files)    # 실제 파일 바이너리를 FileStorage라는 객체 형태로 받아옴

    file = request.files['file']
    print(file)

    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'
    
    max_size = 1 * 1024 * 1024
    if get_filesize(file) > max_size:
        return f'첨부 가능한 용량은 {max_size // 1024}KB입니다.'

    if allowed_file(file.filename):
        file_path = os.path.join('./', UPLOAD_FOLDER, file.filename.replace(' ','_'))
        file.save(file_path)
        return redirect(url_for('index')) #index 함수가 가지고 있는 라우터 주소로 이동하라는 뜻
    
    return '허용되지 않는 파일입니다.'

# @app.route('/delete/<filename>', methods=['GET'])
@app.route('/delete/<filename>', methods=['POST'])
def remove_file(filename):
    file_path = os.path.join('./', UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
    except FileNotFoundError:
        return '파일이 존재하지 않거나 이미 삭제되었습니다.'
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)