from flask import Flask, request, url_for, jsonify, send_from_directory
from csvControl import add_to_csv, get_images, set_keywords, UPLOAD_FOLDER
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/admin')
def admin():
    return send_from_directory(app.static_folder, 'admin.html')

@app.route('/api/list')
def all_list():
    images = get_images()
    return jsonify(images)

@app.route('/api/search')
def search():
    images = get_images()
    q = request.args.get('q', '').lower()
    results = [url_for('static', filename=f"img/{item['filename']}") for item in images if q in item['keyword']]
    return jsonify({'url':results})

@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files['file']
    replaced_filename = file.filename.replace(' ','_')
    file_path = os.path.join('./', UPLOAD_FOLDER, replaced_filename)
    file.save(file_path)

    for item in get_images():
        if item['filename'] == replaced_filename:
            return jsonify({'msg':'success'})
    
    add_to_csv(replaced_filename)
    return jsonify({'msg':'success'})

@app.route('/api/update-keyword/<filename>', methods=['POST'])
def update_keyword(filename):
    new_keyword = request.form.get('newKeyword')
    set_keywords(filename, new_keyword)
    return jsonify({'msg':'success'})

@app.route('/api/delete/<filename>', methods=['POST'])
def delete(filename):
    file_path = os.path.join('./', UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
    except FileNotFoundError:
        return jsonify({'msg':'file not found'})
    return jsonify({'msg':'success'})

if __name__ == '__main__':
    print('current server: fe_admin_restapi')
    app.run(debug=True)
