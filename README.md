# 📝 ToDo App

A simple Django-based todo application to manage your tasks efficiently!

## Setup 🚀

To get started with this repository, follow these steps:

1. **Clone the repository:**

```bash
git clone https://github.com/SAURABHSINGHDHAMI/todo.git
```

2. **Create migrations:**

```bash
py manage.py makemigrations
```

3. **Apply migrations:**

```bash
py manage.py migrate
```

4. **Create an admin user:**

```bash
py manage.py createsuperuser
```

Follow the prompts to set up the admin username, password, and email.

5. **Now, start the server:**

```bash
py manage.py runserver
```

## Features 🌟

- Add, edit, and delete tasks.
- Set start and end times for tasks.
- Add notes to tasks.
- Mark tasks as completed.
- User-friendly interface with Bootstrap styling.

## Usage 💡

- Visit the home page to view and manage your tasks.
- Add new tasks using the form at the bottom of the task list.
- Edit or delete existing tasks using the provided buttons.
- Check off completed tasks by clicking the checkbox.
- Tasks are automatically sorted by start time for easy management.

## Dependencies 🛠️

Ensure you have the following dependencies installed:

- asgiref==3.8.1
- Django==5.0.4
- sqlparse==0.5.0
- tzdata==2024.1
