import mysql.connector
from mysql.connector import Error


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
        cursor.commit()


def connect_to_prodev():
    pass


def create_table(connection):
    pass


def insert_data(connection, csv_file):
    pass
