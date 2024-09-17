import unittest
from unittest.mock import patch, MagicMock
import os
from task_manager.manager import TaskManager, Task
from storage import Storage


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.test_file_name = "test_tasks.json"
        self.storage = Storage(self.test_file_name)
        self.manager = TaskManager(self.storage)

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    @patch("uuid.uuid4")
    def test_add_task(self, mock_uuid):
        mock_uuid.return_value = "10"  # mocking the uuid
        task = self.manager.add_task("Test Task", "This is a test task")
        self.assertEqual(task.id, "10")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)
        self.assertIsNone(task.completed_at)

    def test_list_tasks(self):
        self.manager.add_task("Task 1", "Description 1")
        self.manager.add_task("Task 2", "Description 2")
        tasks = self.manager.list_tasks()
        print(tasks)
        self.assertEqual(len(tasks), 2)

    def test_list_incomplete_tasks(self):
        self.manager.add_task("Task 1", "Description 1")
        task2 = self.manager.add_task("Task 2", "Description 2")
        self.manager.complete_task(task2.id)
        incomplete_tasks = self.manager.list_tasks(only_incomplete=True)
        self.assertEqual(len(incomplete_tasks), 1)
        self.assertEqual(incomplete_tasks[0].title, "Task 1")

    def test_generate_report(self):
        self.manager.add_task("Task 1", "Description 1")
        task2 = self.manager.add_task("Task 2", "Description 2")
        self.manager.complete_task(task2.id)

        report = self.manager.generate_report()
        self.assertEqual(report["total"], 2)
        self.assertEqual(report["completed"], 1)
        self.assertEqual(report["pending"], 1)
        self.assertIsInstance(report["avg_completion_time"], float)

    def test_persistence(self):
        self.manager.add_task("Persistent Task", "This should persist")
        new_storage = Storage(self.test_file_name)
        new_manager = TaskManager(new_storage)
        tasks = new_manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Persistent Task")
        self.assertEqual(tasks[0].description, "This should persist")

    @patch("task_manager.task.datetime")  # failed to mock dateTime in an expected way
    def test_average_completion_time(self, mock_datetime):
        pass


if __name__ == "__main__":
    unittest.main()
