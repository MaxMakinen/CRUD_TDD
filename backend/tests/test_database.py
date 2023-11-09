import sqlite3
import os

def is_database_present(db_path):
    return os.path.exists(db_path)

def is_table_present(db_path, table_name):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name= '{table_name}'")
        return cursor.fetchone is not None