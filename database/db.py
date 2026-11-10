
import sqlite3
from pathlib import Path

# Database file location
DB_PATH = Path(__file__).resolve().parent / "student_hub.db"


# Create the assignments table
def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                due_date TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        """)


# Add a new assignment
def add_assignment(title, subject, due_date):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO assignments
            (title, subject, due_date)
            VALUES (?, ?, ?)
            """,
            (title, subject, due_date)
        )


# Retrieve all assignments
def get_assignments():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("""
            SELECT id, title, subject, due_date, completed
            FROM assignments
            ORDER BY completed ASC, due_date ASC
        """).fetchall()


# Change assignment completion status
def update_assignment(assignment_id, completed):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            UPDATE assignments
            SET completed = ?
            WHERE id = ?
            """,
            (completed, assignment_id)
        )


# Delete an assignment
def delete_assignment(assignment_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "DELETE FROM assignments WHERE id = ?",
            (assignment_id,)
        )

# ==================================
# NOTES MANAGEMENT FUNCTIONS
# ==================================

# Create notes table
def init_notes_table():

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


# Add a new note
def add_note(title, subject, content):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            INSERT INTO notes (title, subject, content)
            VALUES (?, ?, ?)
        """, (title, subject, content))


# Retrieve all notes
def get_notes():

    with sqlite3.connect(DB_PATH) as conn:

        return conn.execute("""
            SELECT id, title, subject, content, created_at
            FROM notes
            ORDER BY id DESC
        """).fetchall()


# Update an existing note
def update_note(note_id, title, subject, content):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            UPDATE notes
            SET title = ?, subject = ?, content = ?
            WHERE id = ?
        """, (title, subject, content, note_id))


# Delete a note
def delete_note(note_id):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            DELETE FROM notes
            WHERE id = ?
        """, (note_id,))

# ==================================
# PROJECT TRACKER DATABASE FUNCTIONS
# ==================================

# Create projects table
def init_projects_table():

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                status TEXT NOT NULL,
                priority TEXT NOT NULL,
                technologies TEXT,
                progress INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


# Add a new project
def add_project(
    name,
    description,
    start_date,
    end_date,
    status,
    priority,
    technologies,
    progress
):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            INSERT INTO projects (
                name,
                description,
                start_date,
                end_date,
                status,
                priority,
                technologies,
                progress
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            description,
            start_date,
            end_date,
            status,
            priority,
            technologies,
            progress
        ))


# Retrieve all projects
def get_projects():

    with sqlite3.connect(DB_PATH) as conn:

        return conn.execute("""
            SELECT
                id,
                name,
                description,
                start_date,
                end_date,
                status,
                priority,
                technologies,
                progress
            FROM projects
            ORDER BY id DESC
        """).fetchall()


# Update an existing project
def update_project(
    project_id,
    name,
    description,
    start_date,
    end_date,
    status,
    priority,
    technologies,
    progress
):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            UPDATE projects
            SET
                name = ?,
                description = ?,
                start_date = ?,
                end_date = ?,
                status = ?,
                priority = ?,
                technologies = ?,
                progress = ?
            WHERE id = ?
        """, (
            name,
            description,
            start_date,
            end_date,
            status,
            priority,
            technologies,
            progress,
            project_id
        ))


# Delete a project
def delete_project(project_id):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute("""
            DELETE FROM projects
            WHERE id = ?
        """, (project_id,))
