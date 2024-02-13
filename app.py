from flask import Flask, render_template, request, redirect, url_for, flash
from todo_service import TodoService

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# We initialize the service
todo_service = TodoService()

@app.route('/')
def index():
    tasks = todo_service.get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form['content']
    todo_service.add_task(task_content)
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    todo_service.complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/clear_tasks', methods=['POST'])
def clear_tasks():
    todo_service.clear_tasks()
    flash('All tasks cleared successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
