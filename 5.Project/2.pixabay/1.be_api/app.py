from flask import Flask, url_for, jsonify
import random

app = Flask(__name__)

dog_images = [f'dog{i}.jpeg' for i in range(1, 6)]

@app.route('/random-dog')
def random_dog():
    random_img = random.choice(dog_images)
    image_url = url_for('static', filename=f'img/{random_img}', _external=True)
    return jsonify({'url':image_url})

if __name__ == '__main__':
    app.run(debug=True)