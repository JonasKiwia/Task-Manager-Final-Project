from datetime import datetime
from models.project import Project
from models.task import Task

def exit_program():
    print("Thank you for using TaskMaster! Goodbye!")
    exit()

# Project helpers
def create_project():
    print("\n=== Create New Project ===")
    try:
        name = input("Project name: ")
        description = input("Project description (optional): ")
        project = Project.create(name=name, description=description)
        print(f"Project '{project.name}' created successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def list_projects():
    projects = Project.get_all()
    if not projects:
        print("\nNo projects found. Create one first!")
        return None
    
    print("\n=== Projects ===")
    for project in projects:
        task_count = len(project.tasks)
        print(f"{project.id}. {project.name} ({task_count} tasks)")
    return projects

def view_project():
    projects = list_projects()
    if not projects:
        return
    
    try:
        project_id = int(input("\nEnter project ID to view: "))
        project = Project.find_by_id(project_id)
        if not project:
            print(f"No project found with ID {project_id}")
            return
        
        print(f"\n=== Project: {project.name} ===")
        print(f"Description: {project.description}")
        print(f"Created: {project.created_at.strftime('%Y-%m-%d')}")
        
        tasks = Task.find_by_project(project_id)
        if not tasks:
            print("No tasks in this project yet.")
        else:
            print("\nTasks:")
            for task in tasks:
                status = "✓" if task.completed else " "
                priority_map = {1: "Low", 2: "Medium", 3: "High"}
                print(f"[{status}] {task.id}. {task.title} (Priority: {priority_map[task.priority]})")
    except ValueError:
        print("Please enter a valid project ID (number)")

def delete_project():
    projects = list_projects()
    if not projects:
        return
    
    try:
        project_id = int(input("\nEnter project ID to delete: "))
        project = Project.find_by_id(project_id)
        if not project:
            print(f"No project found with ID {project_id}")
            return
        
        confirm = input(f"Are you sure you want to delete '{project.name}' and all its tasks? (y/n): ")
        if confirm.lower() == 'y':
            project.delete()
            print(f"Project '{project.name}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Please enter a valid project ID (number)")

def find_project_by_name():
    name = input("\nEnter project name to find: ")
    project = Project.find_by_name(name)
    if project:
        print(f"\nFound project: {project.id}. {project.name}")
        print(f"Description: {project.description}")
        print(f"Created: {project.created_at.strftime('%Y-%m-%d')}")
    else:
        print(f"No project found with name '{name}'")

# Task helpers
def create_task():
    projects = list_projects()
    if not projects:
        return
    
    try:
        project_id = int(input("\nEnter project ID for this task: "))
        project = Project.find_by_id(project_id)
        if not project:
            print(f"No project found with ID {project_id}")
            return
        
        title = input("Task title: ")
        description = input("Task description (optional): ")
        
        priority = None
        while priority not in [1, 2, 3]:
            try:
                priority = int(input("Priority (1=Low, 2=Medium, 3=High): "))
                if priority not in [1, 2, 3]:
                    print("Please enter 1, 2, or 3 for priority")
            except ValueError:
                print("Please enter a number for priority")
        
        due_date_str = input("Due date (YYYY-MM-DD) (optional): ")
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. No due date set.")
        
        task = Task.create(
            title=title,
            description=description,
            priority=priority,
            project_id=project_id,
            due_date=due_date
        )
        print(f"Task '{task.title}' created successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def list_tasks():
    tasks = Task.get_all()
    if not tasks:
        print("\nNo tasks found. Create one first!")
        return None
    
    print("\n=== All Tasks ===")
    for task in tasks:
        status = "✓" if task.completed else " "
        priority_map = {1: "Low", 2: "Medium", 3: "High"}
        print(f"[{status}] {task.id}. {task.title} (Project: {task.project.name}, Priority: {priority_map[task.priority]})")
    return tasks

def mark_task_status():
    tasks = list_tasks()
    if not tasks:
        return
    
    try:
        task_id = int(input("\nEnter task ID to update status: "))
        task = Task.find_by_id(task_id)
        if not task:
            print(f"No task found with ID {task_id}")
            return
        
        current_status = "completed" if task.completed else "pending"
        print(f"Task '{task.title}' is currently {current_status}")
        
        if task.completed:
            confirm = input("Mark as incomplete? (y/n): ")
            if confirm.lower() == 'y':
                task.mark_incomplete()
                print("Task marked as incomplete!")
        else:
            confirm = input("Mark as completed? (y/n): ")
            if confirm.lower() == 'y':
                task.mark_completed()
                print("Task marked as completed!")
    except ValueError:
        print("Please enter a valid task ID (number)")

def delete_task():
    tasks = list_tasks()
    if not tasks:
        return
    
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        task = Task.find_by_id(task_id)
        if not task:
            print(f"No task found with ID {task_id}")
            return
        
        confirm = input(f"Are you sure you want to delete '{task.title}'? (y/n): ")
        if confirm.lower() == 'y':
            task.delete()
            print(f"Task '{task.title}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Please enter a valid task ID (number)")