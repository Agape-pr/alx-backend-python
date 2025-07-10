import mysql.connector
from mysql.connector import errorcode

def connect_db():
    """Connect to MySQL server without specifying a database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Change if your MySQL host is different
            user='your_username',    # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()


import mysql.connector
from mysql.connector import Error

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',         # or your MySQL host
            user='your_mysql_user',   # replace with your MySQL username
            password='your_password', # replace with your MySQL password
            database='ALX_prodev'     # connect to this database
        )
        if connection.is_connected():
            print("Connected to ALX_prodev database")
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        )
    """)
    connection.commit()
    cursor.close()



import csv
import uuid

def insert_data(connection, data):
    try:
        cursor = connection.cursor()

        with open(data, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Generate UUID for each user
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']

                # Check if email already exists to avoid duplicates
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
                result = cursor.fetchone()

                if not result:
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (user_id, name, email, age))

        connection.commit()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()
