
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="DevSecOps Pipeline API")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pipeline (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stage TEXT,
        status TEXT
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM pipeline")
    count = cursor.fetchone()[0]

    if count == 0:
        data = [
            ("Build", "Passed"),
            ("Testing", "Passed"),
            ("Security Scan", "Secure"),
            ("Docker", "Running"),
            ("Deploy", "Pending")
        ]
        cursor.executemany(
            "INSERT INTO pipeline(stage,status) VALUES (?,?)", data
        )

    conn.commit()
    conn.close()

init_db()

@app.get("/")
def home():
    return {
        "message": "DevSecOps Backend Running"
    }

@app.get("/api/status")
def get_status():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT stage,status FROM pipeline")
    rows = cursor.fetchall()

    conn.close()

    result = []

    for row in rows:
        result.append({
            "stage": row[0],
            "status": row[1]
        })

    return result

@app.get("/api/commit")
def latest_commit():
    return {
        "commit": "Initial project structure",
        "author": "Harini",
        "branch": "main"
    }