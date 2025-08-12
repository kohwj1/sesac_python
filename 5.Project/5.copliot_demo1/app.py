from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todo', methods=['POST'])
def add_todo():
    todo_data = request.json
    if 'todo' in todo_data:
        new_todo = todo_data['todo']
        todos.append(new_todo)
        return jsonify({'message': 'Todo added successfully'}), 201
    else:
        return jsonify({'error': 'Missing todo field in request'}), 400

@app.route('/todo/<todo_id>', methods=['PUT'])
def mark_as_completed(todo_id):
    if todo_id < len(todos):
        todos[todo_id] = todos[todo_id] + " (Completed)"
        return jsonify({'message': 'Todo marked as completed'}), 200
    else:
        return jsonify({'error': 'Todo id not found'}), 404

@app.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo_item(todo_id):
    if todo_id < len(todos):
        del todos[todo_id]
        return jsonify({'message': 'Todo item deleted'}), 200
    else:
        return jsonify({'error': 'Todo id not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)