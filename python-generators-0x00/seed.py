import mysql.connector
from mysql.connector import Error


def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS ALX_prodev"
        )
        print("Database created successfully")
    except Error as e:
        print(f"Error occured while creating database {e}")
        return None
    finally:
        connection.commit()


def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='ALX_prodev',
            user='root',
            password='Zootopia.1'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='ALX_prodev',
            user='root',
            password='password'
        )
        if connection.is_connected():
            print("Connected to ALX_prodev database")
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS user_data(
                            user_id BINARY(16) PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            email VARCHAR(100) NOT NULL,
                            age INT NOT NULL
                            )
            """)
        connection.commit()
    except Error as e:
        print(f"Found an error while creating a table {e}")

    finally:
        cursor.close()


def insert_data(connection, filename):
    cursor = connection.cursor()
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, email, age = line.strip().split(',')
                cursor.execute(
                    "INSERT INTO user_data (name, email, age) VALUES (%s, %s, %s)",
                    (name, email, age)
                )
        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

    # insert_data(connect_to_prodev(), 'data.txt')
