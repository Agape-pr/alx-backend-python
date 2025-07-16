import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None
        self.result = None

    def __enter__(self):
        # Connect to DB
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        # Execute the query
        cursor.execute(self.query, self.params)
        self.result = cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
