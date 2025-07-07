from flask import Flask

app = Flask(__name__) #__name__: 현재 파일명을 이름으로 사용할 수 있음 (파일명 그대로 사용해야 할 때 관행적으로 사용)

@app.route('/')
def home():

    return """
    <html>
    <head>
    </head>
    <body>
        <h1>hello Flask!</h1>
        <h2>안녕하세요</h2>
        <p>상품목록</p>
        <div>
            <ul>
                <li>아메리카노</li>
                <li>아메리카노</li>
                <li>아메리카노</li>
            </ul>
        </div>
    </body>
    </html>    
    """

if __name__ == '__main__':
    app.run(debug=True)
