import sqlite3
import os
import logging

class KeyDatabase:
    def __init__(self):
        self.db_path = os.path.join('uploads', 'keys', 'keys.db')
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key_name TEXT NOT NULL,
            key_data BLOB NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()
        conn.close()

    def save_key(self, key_name, key_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO keys (key_name, key_data) VALUES (?, ?)', (key_name, key_data))
        conn.commit()
        conn.close()

    def get_all_keys(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, key_name, created_at FROM keys ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_key(self, key_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM keys WHERE id = ?', (key_id,))
        conn.commit()
        conn.close()
