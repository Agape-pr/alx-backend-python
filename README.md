# 🌀 ALX Backend Python – Generators & SQL Streaming

Welcome to the **Python Generators and SQL Integration Module** of the ALX Backend curriculum.  
This project demonstrates how to work with **Python generators**, large datasets, and **real-time SQL streaming** in a memory-efficient way.

---

## 📚 Project Overview

This module focuses on using Python’s `yield` and generator functions to process data **efficiently** and **incrementally** — an essential skill for backend developers working with **large datasets**, **streaming applications**, and **live dashboards**.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- ✅ Create Python **generator functions** using `yield`
- ✅ Stream data from a **SQL database row-by-row**
- ✅ Handle **large datasets** without overloading memory
- ✅ Simulate **real-world streaming behavior**
- ✅ Use **SQL queries dynamically** inside Python
- ✅ Integrate **Python + MySQL/SQLite** for high-performance data access
- ✅ Compute aggregations like **average age** without loading full datasets

---

## 🔧 Technologies & Tools

- **Python 3.x**
- **MySQL** (via `mysql-connector-python`)
- **CSV for data seeding**
- **UUIDs** and indexed primary keys
- **SQL performance profiling (EXPLAIN, LIMIT, OFFSET)**

---

## 🚀 Getting Started

### Setup

1. Clone the repository:
```bash
git clone https://github.com/BlessingEbele/alx-backend-python.git
cd alx-backend-python/python-generators-0x00
Install dependencies:

bash
pip install mysql-connector-python
Update your MySQL credentials in seed.py, then run:

bash
chmod +x 0-main.py
./0-main.py

📁 Project Structure
bash
alx-backend-python/
└── python-generators-0x00/
    ├── 0-main.py                  # DB setup and seeding test
    ├── seed.py                    # MySQL setup, table creation, CSV seeding
    ├── user_data.csv              # Sample data (UUID, name, email, age)
    ├── 0-stream_users.py          # Generator to stream users row-by-row
    ├── 1-main.py                  # Tests stream_users()
    ├── 1-batch_processing.py      # Batch streaming and age filtering
    ├── 2-main.py                  # Tests batch_processing()
    ├── 2-lazy_paginate.py         # Lazy page streaming using LIMIT/OFFSET
    ├── 3-main.py                  # Tests lazy pagination
    ├── 4-stream_ages.py           # Generator for memory-efficient avg age
    ├── 4-main.py                  # Tests compute_average_age()
    └── README.md                  # This file
✅ Tasks Breakdown
0. Seed the MySQL Database
Creates ALX_prodev database

Adds a user_data table with:

user_id (UUID PRIMARY KEY)

name, email, age

Seeds from user_data.csv

✅ Output preview:

bash
connection successful
Database ALX_prodev is present
[('UUID', 'Name', 'Email', Age), ...]
1. Stream SQL Rows One-by-One
File: 0-stream_users.py

Implements:

python
def stream_users():
    # Yields each user row one at a time using `yield`
✅ Memory-efficient iteration with one loop
✅ Tested with 1-main.py

2. Batch Processing with Filtering
File: 1-batch_processing.py

Implements:

python
def stream_users_in_batches(batch_size):
def batch_processing(batch_size):
    # Filters users over age 25 in batches
✅ Batch streaming with max 3 loops
✅ Tested with 2-main.py

3. Lazy Loading Paginated Data
File: 2-lazy_paginate.py

Uses LIMIT + OFFSET to simulate pagination on-demand.

Implements:

python
def lazy_pagination(page_size):
    # Uses a generator to lazily load next page of users
✅ Only loads one page at a time
✅ Tested with 3-main.py

4. Memory-Efficient Aggregation
File: 4-stream_ages.py

Implements:

python
def stream_user_ages():
    # Yields each user’s age one by one

def compute_average_age():
    # Calculates average age using only two variables
✅ No SQL AVG()
✅ Uses generator and ≤ 2 loops
✅ Prints: Average age of users: 64.87
✅ Tested with 4-main.py

✍️ Author
Blessing Ebele Anochili
Backend Developer | Python Enthusiast | ALX SE Program
🔗 GitHub: github.com/BlessingEbele
🌍 Lagos, Nigeria

🔖 License
This project is part of the ALX Software Engineering Program and follows the ALX academic submission requirements.
