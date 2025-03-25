def show_task(list):
    if not list:
        print("No tasks")
    else:
        print("List of Tasks: ")
        for i, task in enumerate(list, start=0):
            print(f"{i + 1}. {task}")

def add_task(list):
    try:
        task = input("Enter task: ").strip()
        if not task:
            raise ValueError("Task cannot be empty")
        list.append(task)
        print(f"Task '{task}' added")
    except ValueError as e:
        print(f"Error: {e}")

def delete_task(list):
    try:
        if not list:
            raise ValueError("No tasks to delete")
        
        show_task(list)
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(list):
            raise IndexError("Invalid task number")
        
        task = list.pop(task_number - 1)
        print(f"Task '{task}' deleted")
    
    except ValueError:
        print("Error: Invalid task number")
    except IndexError as e:
        print(f"Error: {e}")

def main():
    tasks = []
    while True:
        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
    
if __name__ == "__main__":
    main()