from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
# ALLOWED_FILE_EXT = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif'} #중복체크

os.makedirs(UPLOAD_FOLDER, exist_ok=True) #폴더 생성 (있어도 허용)

def allowed_file(filename:str):
    # if '.' not in filename:
    #     return False
    
    # ext = filename.rsplit('.', 1)[1].lower()
    # return ext in ALLOWED_FILE_EXT

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT


@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    #file = request.form    # 속성, 파일명만 받아옴
    print(request.files)    # 실제 파일 바이너리를 FileStorage라는 객체 형태로 받아옴

    file = request.files['file']
    print(file)

    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'

    if allowed_file(file.filename):
        file_path = os.path.join('./', UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return '파일 업로드 완료'
    
    return '허용되지 않는 파일입니다.'

if __name__ == '__main__':
    app.run(debug=True)