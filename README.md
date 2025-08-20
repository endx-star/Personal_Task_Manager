# Personal Task Manager

A small, maintainable desktop task manager built with Python (Tkinter) and PostgreSQL. The app persists tasks in a PostgreSQL database and loads connection settings from a local `.env` file.

## Tech stack
- Python (3.8+)
- Tkinter (desktop UI)
- PostgreSQL (data store)
- psycopg2 (database driver)
- python-dotenv (environment variable loading)

## Prerequisites
- Python 3.8 or newer
- A running PostgreSQL instance and credentials with permissions to create tables

## Installation
Install the Python dependencies:
```bash
# Windows
py -m pip install psycopg2-binary python-dotenv
# macOS/Linux
pip3 install psycopg2-binary python-dotenv
```

## Configuration
Create a `.env` file in `Personal_Task_Manager/` with the following variables:
```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```
Notes:
- `.env` is git-ignored and should not be committed.
- The application validates `DB_NAME`, `DB_USER`, and `DB_PASSWORD` on startup.

## Run
From the repository root:
```bash
cd Personal_Task_Manager
# Windows
py -3 main.py   # or: python main.py
# macOS/Linux
python3 main.py
```
On first launch, the schema is initialized automatically (table `tasks` is created if missing).

## Features
- Add, view, update, and delete tasks
- Persistent storage in PostgreSQL
- Simple, responsive Tkinter UI

## Troubleshooting
- ModuleNotFoundError: No module named 'dotenv' → Install `python-dotenv` as shown above.
- psycopg2.OperationalError (auth/connection) → Verify `.env` values and that PostgreSQL is reachable.
- UndefinedTable: relation "tasks" does not exist → The app initializes the table on startup; ensure the app has permissions to create tables.

## Project structure
- `main.py` — Application entry point; initializes DB and launches the UI
- `ui.py` — Tkinter user interface (windows, forms, actions)
- `task_manager.py` — High-level operations orchestrating DB actions
- `db.py` — DB connection management, schema init, and CRUD functions
- `task.py` — Task model
