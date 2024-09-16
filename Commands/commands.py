class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement execute method")


class AddTaskCommand(Command):
    def __init__(self, manager, title, description):
        self.manager = manager
        self.title = title
        self.description = description

    def execute(self):
        task = self.manager.add_task(self.title, self.description)
        print(f"Task '{task.title}' added successfully.")
        print(f"Description: {task.description}")
        print(f"Task ID: {task.id}")


class CompleteTaskCommand(Command):
    def __init__(self, manager, task_id):
        self.manager = manager
        self.task_id = task_id

    def execute(self):
        if self.manager.complete_task(self.task_id):
            print(f"Task with ID '{self.task_id}' marked as completed.")
        else:
            print(f"Task with ID '{self.task_id}' not found.")


class ListTasksCommand(Command):
    def __init__(self, manager, only_incomplete):
        self.manager = manager
        self.only_incomplete = only_incomplete

    def execute(self):
        tasks = self.manager.list_tasks(only_incomplete=self.only_incomplete)
        if tasks:
            for task in tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"ID: {task.id}, Title: {task.title}, Status: {status}")
                print(f"Description: {task.description}")
                print("-" * 20)
        else:
            print("No tasks found.")


class GenerateReportCommand(Command):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        report = self.manager.generate_report()
        print(f"Total tasks: {report['total']}")
        print(f"Completed tasks: {report['completed']}")
        print(f"Pending tasks: {report['pending']}")
        print(f"Average completion time: {report['avg_completion_time']} hours")


def create_command(manager, args):
    if args.command == "add":
        return AddTaskCommand(manager, args.title, args.description)
    elif args.command == "complete":
        return CompleteTaskCommand(manager, args.id)
    elif args.command == "list":
        return ListTasksCommand(manager, args.incomplete)
    elif args.command == "report":
        return GenerateReportCommand(manager)
    else:
        return None
