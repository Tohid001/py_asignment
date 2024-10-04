# Task Management System

This simple command-line (CLI) task management system is implemented in Python.

## Functional Requirements

The application should allow users to do the following:

1. Add a new task
2. Complete a task
3. List all tasks (with an option to show only incomplete tasks)
4. Generate a report of task statistics, which should include:
   - Total number of tasks
   - Number of completed tasks
   - Number of pending tasks
   - Average time taken to complete a task
5. The application must persist user data across sessions, ensuring that all information remains intact and accessible upon returning, without resetting or losing any previously entered tasks

## Setup

1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Install Poetry if you don't have it installed:
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
5. Install dependencies
    ```
    poetry install
    ```
6.  Running the application
    ```
    poetry run python main.py
    ```

## Running Tests

To run all the unit tests, use the following command:

```
python -m unittest discover tests
```

## Final output
Commands for  CLI tool

1. poetry run python main.py add --title "New Task" --description "Task description"   (add a task using title and description. both are required)
2. poetry run python main.py list   (all tasks)
3. poetry run python main.py list --incomplete   (only incomplete tasks)
4. poetry run python main.py complete id    (complete task by Id. Id is required)

