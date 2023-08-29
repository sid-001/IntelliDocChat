import sqlite3

class KnowledgeBase:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge_base (
                name TEXT PRIMARY KEY,
                path TEXT
            )
        ''')
        self.conn.commit()
    
    def entry_exists(self, name):
        self.cursor.execute('SELECT EXISTS(SELECT 1 FROM knowledge_base WHERE name = ?)', (name,))
        return self.cursor.fetchone()[0] == 1

    def insert_entry(self, name, path):
        try:
            self.cursor.execute('INSERT INTO knowledge_base (name, path) VALUES (?, ?)', (name, path))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_entry_by_name(self, name):
        self.cursor.execute('SELECT * FROM knowledge_base WHERE name = ?', (name,))
        return self.cursor.fetchone()

    def get_all_entries(self):
        self.cursor.execute('SELECT * FROM knowledge_base')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
        return True

# Example usage
if __name__ == '__main__':
    kb = KnowledgeBase()
    kb.insert_entry("entry1", "/path/to/entry1")
    kb.insert_entry("entry2", "/path/to/entry2")
    kb.insert_entry("entry1", "/new/path/to/entry1")  # This will raise an IntegrityError
    kb.close_connection()
