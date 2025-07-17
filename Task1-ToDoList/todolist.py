todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks available.")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(todo_list, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    task = {"title": title, "completed": False}
    todo_list.append(task)
    print("Task added.")

def update_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(todo_list):
            new_title = input("Enter new task title: ")
            todo_list[task_num]["title"] = new_title
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_complete():
    show_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            del todo_list[task_num]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_complete()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting To-Do List. Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()