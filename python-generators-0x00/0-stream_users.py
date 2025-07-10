import mysql.connector

def stream_users():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',     # Replace this
            password='your_mysql_password', # Replace this
            database='ALX_prodev'
        )

        cursor = connection.cursor(dictionary=True)  # This returns rows as dictionaries

        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row  # This is the generator: yields one row at a time

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        connection.close()
