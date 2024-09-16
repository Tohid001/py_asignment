from datetime import datetime
from task_manager.task import Task


class TaskManager:

    def __init__(self, storage):
        self.storage = storage

    def add_task(self, title, description):
        task = Task(title, description)
        self.storage.add_task(task)
        return task

    def complete_task(self, task_id):
        task = self.storage.get_task_by_id(task_id)
        if task:
            task.complete()
            self.storage.update_task(task)
            return True
        return False

    def list_tasks(self, only_incomplete=False):
        tasks = self.storage.get_all_tasks()
        if only_incomplete:
            tasks = [task for task in tasks if not task.completed]
        else:
            tasks = [task for task in tasks if task.completed]
        return tasks

    def generate_report(self):
        tasks = self.storage.get_all_tasks()
        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task.completed)
        pending_tasks = total_tasks - completed_tasks

        avg_completion_time = 0
        if completed_tasks > 0:
            completion_times = [
                (
                    datetime.fromisoformat(task.completed_at)
                    - datetime.fromisoformat(task.created_at)
                ).total_seconds()
                / 3600
                for task in tasks
                if task.completed
            ]
            avg_completion_time = sum(completion_times) / len(completion_times)

        return {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks,
            "avg_completion_time": round(avg_completion_time, 2),
        }
