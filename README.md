# TaskMaster: CLI Task Management System

TaskMaster is a command-line task management system built with Python and SQLAlchemy. It allows users to create and manage projects and tasks in an organized manner.

## Features

- Create, view, and manage projects
- Create, view, and manage tasks within projects
- Mark tasks as completed or incomplete
- Set task priorities (Low, Medium, High)
- Set due dates for tasks
- Search for projects by name

## Installation

1. Clone this repository
2. Ensure you have Python 3.8+ installed
3. Install dependencies with Pipenv:

```
pipenv install
pipenv shell
```

4. Set up the database:

```
python lib/debug.py
```

5. Run the application:

```
python lib/cli.py
```

## Usage

### Main Menu

The main menu provides access to project and task management features:

1. Project Management
2. Task Management
0. Exit

### Project Management

- Create new projects with a name and optional description
- List all projects
- View project details, including tasks associated with the project
- Delete projects (this will also delete all tasks associated with the project)
- Find projects by name

### Task Management

- Create new tasks assigned to a specific project
- List all tasks across all projects
- Mark tasks as completed or incomplete
- Delete tasks

## Data Model

TaskMaster uses a simple data model with two main entities:

1. **Project**: Represents a collection of related tasks
   - Attributes: id, name, description, created_at
   - Relationships: Has many tasks

2. **Task**: Represents an individual task to be completed
   - Attributes: id, title, description, priority, completed, created_at, due_date, project_id
   - Relationships: Belongs to a project

## Project Structure

```
taskmaster/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib/
    ├── models/
    │   ├── __init__.py
    │   ├── project.py
    │   └── task.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

## Module Descriptions

- **models/__init__.py**: Sets up the database connection and session
- **models/project.py**: Defines the Project model with ORM methods
- **models/task.py**: Defines the Task model with ORM methods
- **cli.py**: Main CLI interface with menu system
- **debug.py**: Utility script for database setup
- **helpers.py**: Helper functions for CLI operations

## Future Enhancements

- Task filtering and sorting
- Task categories/tags
- Recurring tasks
- Due date reminders
- Data visualization (task completion rates, etc.)
- Export/import functionality

## License

This project is licensed under the MIT License - see the LICENSE file for details.