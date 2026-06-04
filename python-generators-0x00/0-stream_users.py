import mysql.connector
from mysql.connector import Error
from itertools import islice


def stream_users():
    """A generator function that connects to a MySQL database and yields user data as dictionaries."""
    cursor = None
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Zootopia.1',
            database='ALX_prodev'
        )

        cursor = connection.cursor(dictionary=True, buffered=True)
        cursor.execute("SELECT * FROM user_data")

        # row = cursor.fetchone()
        # while row is not None:
        #     yield row
        #     row = cursor.fetchone()
        # print("Rows yielded")

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True, buffered=True)
            cursor.execute("SELECT * FROM user_data")
            for row in cursor:
                yield row

    except Error as e:
        print(f"Error while fetching data {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
