import json

class TodoService:
    def __init__(self):
        self.tasks_file = 'tasks.json'

    def get_tasks(self):
        with open(self.tasks_file, 'r') as f:
            tasks = json.load(f)
        return tasks

    def save_tasks(self, tasks):
        with open(self.tasks_file, 'w') as f:
            json.dump(tasks, f)

    def add_task(self, content):
        tasks = self.get_tasks()
        tasks.append({'content': content, 'done': False})
        self.save_tasks(tasks)

    def complete_task(self, task_id):
        tasks = self.get_tasks()
        tasks[task_id]['done'] = True
        self.save_tasks(tasks)

    def clear_tasks(self):
        tasks = []
        self.save_tasks(tasks)