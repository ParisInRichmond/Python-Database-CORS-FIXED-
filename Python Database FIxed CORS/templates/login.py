import sqlite3  # Import the sqlite3 library to work with SQLite databases
import hashlib  # Import the hashlib library to hash passwords for security

# Connect to a SQLite database named 'userdata.db'. If the database does not exist, it will be created.
conn = sqlite3.connect('userdata.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute an SQL command to create a table named 'userdata' if it does not already exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        Id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

# Define username and password pairs, and hash the passwords using SHA-256
username1, password1 = "ManMan", hashlib.sha256("ManManDidIT".encode()).hexdigest()
username2, password2 = "MotherChild", hashlib.sha256("JohnCarter".encode()).hexdigest()
username3, password3 = "ZombieCraft", hashlib.sha256("MineCraftLove".encode()).hexdigest()
username4, password4 = "LucySmith", hashlib.sha256("JohnDoe".encode()).hexdigest()
username5, password5 = "PerryTim", hashlib.sha256("TheUnknown".encode()).hexdigest()

# Insert the username and hashed password pairs into the 'userdata' table
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))

conn.commit()
