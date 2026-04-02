import sqlite3
import json
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def init_db():
    conn = sqlite3.connect('kito_memory.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS chat_log 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     role TEXT, content TEXT, embedding TEXT, 
                     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn

def save_to_db(conn, role, content):
    embedding = embed_model.encode(content).tolist()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_log (role, content, embedding) VALUES (?, ?, ?)", 
                   (role, content, json.dumps(embedding)))
    conn.commit()

def load_persistence_history(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM (SELECT * FROM chat_log ORDER BY id DESC LIMIT 12) ORDER BY id ASC")
    return [{'role': r, 'content': c} for r, c in cursor.fetchall()]