from flask import Flask, redirect
from users_route import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/')
def index():
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)




