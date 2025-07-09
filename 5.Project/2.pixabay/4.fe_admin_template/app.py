from flask import Flask, request, render_template, url_for, redirect
from admin_route import admin_bp
from csvControl import get_images

app = Flask(__name__)
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q', '').lower()
    results = [url_for('static', filename=f"img/{item['filename']}") for item in get_images() if q in item['keyword']]
    return render_template('results.html', q=q, results=results)

if __name__ == '__main__':
    app.run(debug=True)
