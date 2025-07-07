from flask import Flask

app = Flask(__name__) #__name__: 현재 파일명을 이름으로 사용할 수 있음 (파일명 그대로 사용해야 할 때 관행적으로 사용)

if __name__ == '__main__':
    print('메인함수')
    app.run()
