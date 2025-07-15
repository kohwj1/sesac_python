from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    keyword = request.args.get('q', default='').strip()
    if keyword:
        stores = db.search_store(keyword)
    else:
        stores = db.get_stores()
    return render_template('index.html', stores=stores, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)