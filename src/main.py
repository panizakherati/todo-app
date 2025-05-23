import json
import os

TODO_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(data):
    with open(TODO_FILE, "w") as f:
        json.dump(data, f, indent=2)


def show_tasks(data):
    if not data:
        print("No tasks found.")
        return
    print("\nyour tasks:")
    for i, task in enumerate(data, 1):
        status = "done" if task.get("completed") else " "
        print(f"{i}.[{status}] {task['title']}")
    print()


def add_task(data, title):
    data.append({"title": title, "completed": False})
    save_tasks(data)
    print(f"tasks added :{title}")


def complete_task():
    pass


def main():
    print("Hello from todo-app!")
    # tasks = load_tasks()


if __name__ == "__main__":
    main()
