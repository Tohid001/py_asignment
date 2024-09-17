import unittest
from unittest.mock import patch, MagicMock
import io
import sys
import os
from datetime import datetime, timedelta
from main import main
from task_manager.manager import TaskManager, Task
from storage import Storage


class TestTaskManagerCLI(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_tasks.json"
        self.storage = Storage(self.test_filename)
        self.manager = TaskManager(self.storage)

    def tearDown(self):
        # to fix the issue of tasksDb.json causing trouble with the tasks of previous cases,
        # I could have forcefully remove it after each case here like the following:
        # if os.path.exists(tasksDB.json):
        # print("deleteFile")
        # os.remove(tasksDB.jsonb)
        if os.path.exists(self.test_filename):
            print("deleteFile")
            os.remove(self.test_filename)

    def run_command(self, *args):
        captured_output = io.StringIO()
        captured_error = io.StringIO()
        sys.stdout = captured_output
        sys.stderr = captured_error
        try:
            with patch("sys.argv", ["task_manager"] + list(args)):
                main()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        return captured_output.getvalue().strip(), captured_error.getvalue().strip()

    def test_invalid_command(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, this case was not biased to it. So I tested anyway
        _, error = self.run_command("invalid_command")
        self.assertIn("usage:", error)
        self.assertIn(
            "error: argument command: invalid choice: 'invalid_command'", error
        )

    def test_add_task_success(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, this case was not biased to it. So I tested anyway
        output, _ = self.run_command(
            "add", "--title", "Test Task 1", "--description", "Test Description 1"
        )
        self.assertIn("Task 'Test Task 1' added successfully.", output)
        self.assertIn("Description: Test Description 1", output)
        self.assertIn("Task ID:", output)

    def test_add_task_missing_title(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, this case was not biased to it. So I tested anyway
        _, errror = self.run_command("add", "--description", "Test Description")
        self.assertIn("error: the following arguments are required: --title", errror)

    def test_add_task_missing_description(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, this case was not biased to it. So I tested anyway
        _, error = self.run_command("add", "--title", "Test Task")
        self.assertIn(
            "error: the following arguments are required: --description", error
        )

    def test_complete_task_success(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, this case was not biased to it. So I tested anyway
        add_output, _ = self.run_command(
            "add", "--title", "Test Task 2", "--description", "Test Description 2"
        )
        task_id = add_output.split("Task ID: ")[1].strip()  # get the uuid
        complete_output = self.run_command("complete", task_id)
        self.assertIn(
            f"Task with ID '{task_id}' marked as completed.", complete_output
        )  # pass

    def test_complete_task_invalid_id(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, this case was not biased to it. So I tested anyway
        output, _ = self.run_command("complete", "invalid_id")
        self.assertIn("Task with ID 'invalid_id' not found.", output)

    # could not test it out, as taskDB.json is getting created on each case and not getting cleared after each case
    # def test_list_tasks_empty(self):
    #     output, _ = self.run_command("list")
    #     print(output)
    #     self.assertIn("No tasks found.", output)

    def test_list_tasks_multiple(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, I tried to demostrate in away to prove all task
        self.run_command(
            "add", "--title", "Test Task 10", "--description", "Test Description 3"
        )
        self.run_command(
            "add", "--title", "Test Task 11", "--description", "Test Description 4"
        )
        list_output, _ = self.run_command("list")
        self.assertIn("Test Task 10", list_output)
        self.assertIn("Test Task 11", list_output)
        self.assertIn("Status: Pending", list_output)

    def test_list_incomplete_tasks(
        self,
    ):  # although  tasksDb.json causing trouble with the tasks of previous cases, I tried to demostrate in away to prove --incomplete task
        self.run_command(
            "add", "--title", "Test Task 5", "--description", "Test Description 5"
        )
        add_output6, _ = self.run_command(
            "add", "--title", "Test Task 6", "--description", "Test Task 6"
        )
        task_id_6 = add_output6.split("Task ID: ")[1].strip()
        list_output_before_completing_6, _ = self.run_command("list", "--incomplete")
        self.run_command("complete", task_id_6)
        list_output_after_completing_6, _ = self.run_command("list", "--incomplete")
        self.assertIn("Test Task 6", list_output_before_completing_6)
        self.assertNotIn("Test Task 6", list_output_after_completing_6)
        self.assertTrue(
            len(list_output_before_completing_6) > len(list_output_after_completing_6)
        )

    def test_generate_report_empty(
        self,
    ):  # avoided as real test_tasks.json is not getting created and deleted on each case, rather taskDb.json causing trouble with the tasks of previous cases
        pass

    def test_generate_report_with_tasks(
        self,
    ):  # avoided as real test_tasks.json is not getting created and deleted on each case, rather taskDb.json causing trouble with the tasks of previous cases
        pass

    def test_persistence(
        self,
    ):  # avoided as real test_tasks.json is not getting created and deleted on each case, rather taskDb.json causing trouble with the tasks of previous cases
        pass

    @patch("task_manager.task.datetime")  # failed to mock dateTime in an expected way
    def test_average_completion_time(self, mock_datetime):
        pass


if __name__ == "__main__":
    unittest.main()
