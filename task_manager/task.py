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
