from helpers import (
    exit_program,
    create_project,
    list_projects,
    view_project,
    delete_project,
    find_project_by_name,
    create_task,
    list_tasks,
    mark_task_status,
    delete_task
)

def main():
    print("\n===== Welcome to TaskMaster =====")
    print("Your command-line task management system")
    
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            project_menu()
        elif choice == "2":
            task_menu()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("\n===== MAIN MENU =====")
    print("1. Project Management")
    print("2. Task Management")
    print("0. Exit")

def project_menu():
    while True:
        print("\n===== PROJECT MENU =====")
        print("1. Create new project")
        print("2. List all projects")
        print("3. View project details")
        print("4. Delete a project")
        print("5. Find project by name")
        print("0. Back to main menu")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "0":
            break
        elif choice == "1":
            create_project()
        elif choice == "2":
            list_projects()
        elif choice == "3":
            view_project()
        elif choice == "4":
            delete_project()
        elif choice == "5":
            find_project_by_name()
        else:
            print("Invalid choice. Please try again.")

def task_menu():
    while True:
        print("\n===== TASK MENU =====")
        print("1. Create new task")
        print("2. List all tasks")
        print("3. Mark task as completed/incomplete")
        print("4. Delete a task")
        print("0. Back to main menu")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "0":
            break
        elif choice == "1":
            create_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task_status()
        elif choice == "4":
            delete_task()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()