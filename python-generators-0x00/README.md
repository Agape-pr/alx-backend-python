# alx-backend-python

# 📊 Task 0: Getting Started with Python Generators and SQL Integration

## Project Directory: `python-generators-0x00`

This task sets up the foundation for generator-based data streaming using Python and SQL.

---

## 🔧 Task Objective

To create a Python script (`seed.py`) that:

- Connects to MySQL
- Creates the `ALX_prodev` database (if it doesn't exist)
- Creates a `user_data` table with specified schema
- Loads sample data from `user_data.csv` using safe insertions

---

## 🧠 Key Concepts

- `mysql.connector` for Python-MySQL integration
- `csv.DictReader()` for row-wise CSV ingestion
- SQL table creation and seeding with safe constraints
- Ignoring duplicate inserts using `INSERT IGNORE`

---

## 📌 Prototypes Implemented

```python
def connect_db(): ...
def create_database(connection): ...
def connect_to_prodev(): ...
def create_table(connection): ...
def insert_data(connection, data): ...
🧪 Usage Example (via 0-main.py)

$ ./0-main.py
connection successful
Table user_data created successfully
Database ALX_prodev is present 
[('uuid', 'name', 'email', age), ...]
✍️ Author
Blessing Ebele Anochili
GitHub: https://github.com/BlessingEbele/
ALX Software Engineering Program
