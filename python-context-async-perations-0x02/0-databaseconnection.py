import sqlite3

class database_conection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    def __exit__(self, exc_typ, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


with database_conection('user_database') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
print(results)