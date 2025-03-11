
def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def main():
    while True:
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()