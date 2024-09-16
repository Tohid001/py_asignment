import uuid
from datetime import datetime


class Task:

    def __init__(self, title, description):
        self.id = str(uuid.uuid4())  # Generate a unique UUID
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None

    def complete(self):
        self.completed = True
        self.completed_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,  # Save the UUID
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["description"])
        task.id = data["id"]
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        task.completed_at = data["completed_at"]
        return task
