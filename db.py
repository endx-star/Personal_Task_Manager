import os
from pathlib import Path

import psycopg2



# Load environment variables from a local .env file in this directory
try:
    from dotenv import load_dotenv
    _ENV_PATH = Path(__file__).resolve().parent / ".env"
    # load_dotenv is safe to call even if the file does not exist
    load_dotenv(_ENV_PATH)
except Exception:
    # If python-dotenv is not installed, environment variables can still be
    # provided via the OS environment. We fail gracefully here.
    pass

# Read database settings from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")




def get_connection():
    """Create and return a PostgreSQL connection."""
    if not DB_NAME or not DB_USER or not DB_PASSWORD:
        raise RuntimeError(
            "Missing required database environment variables. Ensure DB_NAME, "
            "DB_USER, and DB_PASSWORD are set (e.g., in Personal_Task_Manager/.env)."
        )
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def init_db():
    """Initialize the database and create the tasks table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()




