import argparse
from task_manager.manager import TaskManager
from storage import Storage
from Commands.commands import create_command


def main():
    storage = Storage()
    manager = TaskManager(storage)

    parser = argparse.ArgumentParser(description="Task Management System")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparsers.add_parser(
        "add", help="Add a new task(poetry run python main.py add -h)"
    )
    add_parser.add_argument("--title", required=True, help="Task title(required)")
    add_parser.add_argument(
        "--description", required=True, help="Task description(required)"
    )

    complete_parser = subparsers.add_parser(
        "complete",
        help="Mark a task as completed(poetry run python main.py complete -h)",
    )
    complete_parser.add_argument("id", type=str, help="Task ID")

    list_parser = subparsers.add_parser(
        "list", help="List all tasks(poetry run python main.py list -h)"
    )
    list_parser.add_argument(
        "--incomplete", action="store_true", help="Show only incomplete tasks"
    )

    subparsers.add_parser("report", help="Generate a report")

    args = parser.parse_args()

    command = create_command(manager, args)
    if command:
        command.execute()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


# # python main.py add --title "New Task" --description "Task description"
# # python main.py list
# # python main.py list --incomplete
## python main.py complete id
# # python main.py report
