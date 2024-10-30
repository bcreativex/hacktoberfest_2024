class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show!")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "✅ Completed" if task["completed"] else "❌ Pending"
                print(f"{i}. {task['task']} - {status}")

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: '{removed_task['task']}'")
        else:
            print("Invalid task number!")

    def clear_all_tasks(self):
        self.tasks.clear()
        print("All tasks cleared!")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            todo_list.clear_all_tasks()
        elif choice == "6":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1-6.")

if __name__ == "__main__":
    main()
