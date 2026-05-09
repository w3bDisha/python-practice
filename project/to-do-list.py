tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"✅ '{task}' added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\n--- Your Tasks ---")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def mark_done():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        view_tasks()
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = "✅ " + tasks[num-1]
            print("Task marked as done!")
        else:
            print("Invalid number!")

def delete_task():
    view_tasks()
    num = int(input("Enter a number of task to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!")
    else:
        print("Invalid number!")

# Main loop
while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit")
    
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid option! Choose 1-5")