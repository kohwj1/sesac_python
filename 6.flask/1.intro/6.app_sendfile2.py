from flask import Flask, send_file, send_from_directory

app = Flask(__name__) #__name__: 현재 파일명을 이름으로 사용할 수 있음 (파일명 그대로 사용해야 할 때 관행적으로 사용)

@app.route('/')
def home():
    # return send_file(r'static/index.html')
    return send_from_directory('static','index.html')

if __name__ == '__main__':
    app.run(debug=True)
