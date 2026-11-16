"""A small in-memory task manager for the command line."""


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        description = description.strip()
        if not description:
            raise ValueError("Task description cannot be empty.")
        self.tasks.append(description)


def main():
    manager = TaskManager()
    print("Task Manager (tasks are kept until you exit)")
    while True:
        print("\n1. Add a task\n2. List tasks\n3. Quit")
        try:
            choice = input("Choose an option: ").strip()
            if choice == "1":
                description = input("Task description: ")
                try:
                    manager.add_task(description)
                except ValueError as error:
                    print(error)
                else:
                    print("Task added.")
            elif choice == "2":
                if not manager.tasks:
                    print("No tasks yet.")
                for number, task in enumerate(manager.tasks, start=1):
                    print(f"{number}. {task}")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Please choose 1, 2, or 3.")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
