import mysql.connector
from os import environ, path
from dotenv import load_dotenv

# Base folder dir path
base_dir = path.abspath(path.dirname(__file__))
load_dotenv (path.join(base_dir,'.env'))

# Create Database and Setup Connection
# Only run this once otherwise running it again will overwrite data on the current db
try:
    cnx = mysql.connector.connect(
        user = environ.get('Db_Username'),
        password = environ.get('Db_Password'),
        host = environ.get('Db_Host')
    )
    print("Connected to Database")

    # Use Cursor to create database and show database once created
    my_cursor = cnx.cursor()
    my_cursor.execute("CREATE DATABASE flask_react_db;")
    my_cursor.execute("SHOW DATABASES;")
    for db in my_cursor:
        print(db)
        
except Exception as err:
    print(f"Something went wrong: {err}")