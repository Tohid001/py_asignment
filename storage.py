import json
import os
from config import file_name
from task_manager.task import Task


class Storage:
    def __init__(self, filename=file_name):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def get_task_by_id(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task):
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task
                self.save_tasks()
                break

    def get_all_tasks(self):
        return self.tasks
