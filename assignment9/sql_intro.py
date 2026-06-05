#Task 1: Create a New SQLite Database 
import sqlite3 


#Task 3: Populate Tables with Data 
def add_publisher(conn, name):
    try: 
        cursor = conn.cursor()
    #Check for duplicates 
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"Publisher '{name}' is already in the database.")
            return
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        print(f"Publisher '{name}' added.")
    except Exception as e:
        print("Error adding publisher:", e)

def add_magazine(conn, name, publisher_id):
    try: 
        cursor = conn.cursor()
    #Check for duplicates 
        cursor.execute("SELECT id FROM magazines WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"Magazine '{name}' is already in the database.")
            return
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name,publisher_id))
        print(f"Magazine '{name}' added.")
    except Exception as e:
        print("Error adding magazine:", e)

def add_subscriber(conn, name, address):
    try: 
        cursor = conn.cursor()
    #Check for duplicates 
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
            return
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name,address))
        print(f"Subscriber '{name}' added.")
    except Exception as e:
        print("Error adding subscriber:", e)

def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try: 
        cursor = conn.cursor()
    #Check for duplicates 
        cursor.execute("SELECT id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id,))
        if cursor.fetchone():
            print(f"Subscription aleady exists for this subscriber {subscriber_id} and magazine {magazine_id}.")
            return
        cursor.execute("INSERT INTO subscriptions( subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
        print(f"Subscription added for subscriber {subscriber_id}.")
    except Exception as e:
        print("Error adding subscription:", e)

#Task 4: 
def query_all_subscribers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers")
    print("\nAll Subscribers:")
    for row in cursor.fetchall():
        print(row)

def query_magazines_sorted(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    print("\nMagazines Sorted by Name:")
    for row in cursor.fetchall():
        print(row)

def query_magazines_by_publisher(conn, publisher_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT magazines.id, magazines.name, publishers.name
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publisher.id
        WHERE publisher.id = ?
    """, (publisher_id,))
    print(f"\nMagazines for Publisher {publisher_id}:")
    for row in cursor.fetchall():
        print(row)

#Task 2: Define Database Structure 
with sqlite3.connect("../db/magazines.db") as conn:
    print("Database created and connected successfully.")

#Task 3: Populate Tables with Data 
    conn.execute("PRAGMA foreign_keys = 1")


#Task 2:
    cursor = conn.cursor()

    #Create tables: 
    try:    
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)
    except Exception as e: 
        print("Error creating publishers table:", e)
    
    try:
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        )
        """)
    except Exception as e: 
        print("Error creating magazines table:", e)

    try:
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL
        )
        """)
    except Exception as e: 
        print("Error creating subscribers table:", e)

#Create join table (subscriptions):  
    try:
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL, 
            expiration_date TEXT NOT NULL, 
            FOREIGN KEY (subscriber_id) REFERENCEs subscribers(id)
            FOREIGN KEY (magazine_id) REFERENCEs magazines(id)
            UNIQUE (subscriber_id, magazine_id)
        )
        """)
    except Exception as e: 
        print("Error creating subscriptions table:", e)

#Task 3: adding at least 3 entries
    add_publisher(conn, "Rock Time Daily")
    add_publisher(conn, "Time Inc.")
    add_publisher(conn, "National Exploring")

    add_magazine(conn, "Rocks Weekly", 1)
    add_magazine(conn, "Maps Weekly", 2)
    add_magazine(conn, "Exploring 101 Daily", 3)

    add_subscriber(conn, "Jonhson Henderson", "678 Main St")
    add_subscriber(conn, "June August", "121 New St")
    add_subscriber(conn, "Madison henderson", "2121 Willow Rd")

    add_subscription(conn, 1, 1, "2025-12-31")
    add_subscription(conn, 1, 2, "2026-06-01")
    add_subscription(conn, 2, 3, "2025-08-25")
    
    conn.commit()
    #print("Database and tables created successfully.")
    print("Data added successfully.")



    #conn.close()
    #print("Connection closed.")