tasks = []

def display_menu():
    print("To-Do List")
    print("==========")
    print("1. Add a Task")
    print("2. Delete a task")
    print("3. Edit a task")
    print("4. Mark a task as done")
    print("5. View all tasks")
    print("6. Exit")

def add_task():
    name = input("Enter a task here")
    priority = input("Enter priority high, medium or low: ")

    task = {
        "name": name,
        "priority": priority,
        "status" : "pending"
    }

    tasks.append(task)

    print(f"The {name} added successfully")

def delete_task():
    if len(tasks) == 0:
        print("There are no tasks to delete")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]['name']} - {tasks[i]['priority']} - {tasks[i]['status']}")

