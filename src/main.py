import json
import os
TODO_FILE = "tasks.json"

def load_tasks():
    with open(TODO_FILE, 'r') as f:
        return json.load(f)
def save_tasks():
    pass
def show_tasks():
    pass
def add_task():
    pass
def complete_task():
    pass



def main():
    print("Hello from todo-app!")
    tasks = load_tasks()


if __name__ == "__main__":
    main()
