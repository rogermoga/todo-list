# To-Do List Web Application

This is a simple web application built with Python and Flask that allows users to manage their to-do lists. Users can add tasks, mark tasks as completed, and clear all tasks from the list.

## Requirements

- Python 3
- Flask

## Installation

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.

## Usage

1. Run the Flask application with python app.py
2. Access the application in your web browser at `http://localhost:5000`.
3. Use the provided form to add tasks to the list.
4. Click on the task to mark it as completed.
5. Click on the "Clear All Tasks" button to remove all tasks from the list.

## Project Structure

- `app.py`: Flask application that handles routing and user interactions.
- `todo_service.py`: Business logic layer containing the `TodoService` class responsible for task management.
- `tasks.json`: Data access layer containing the JSON file that stores the tasks.
- `templates/index.html`: HTML template for the to-do list interface.

## Three-Layer Architecture

This project follows a three-layer architecture:

1. **Presentation Layer**: Handled by the Flask application (`app.py`) and HTML templates (`templates/index.html`). This layer is responsible for handling user interactions and presenting data to the user.

2. **Business Logic Layer**: Implemented in the `TodoService` class (`todo_service.py`). This layer contains the application's logic, such as handling tasks, adding tasks, marking tasks as completed, and clearing tasks.

3. **Data Access Layer**: Managed by the `tasks.json` file. This layer interacts with the data storage and performs operations such as reading and writing tasks.

