tasks = []

def add_tasks():
    task = input("Add a task: ")
    tasks.append(task)
    print("Task addes Successfully")

def display_task():
    if len(tasks) == 0:
        print("No tasks found")
    else:
        print("Current Tasks")
        for index, task in enumerate(tasks):
            status = "[X]" if task ["status"] == "Done" else "[ ]"
            print(f"{index}. {status} {task['name']}")

        choice = input("Enter the index of the toggle ")