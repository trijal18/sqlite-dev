import sqlite3
import logging

# Configure logging
logging.basicConfig(
    filename="system.log",
    filemode="a",  # Append to the log file
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def setup_users_db():
    """Set up the Users database."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )""")
    conn.commit()
    conn.close()
    logging.info("Users database setup completed.")

def setup_products_db():
    """Set up the Products database."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL CHECK(price > 0)
    )""")
    conn.commit()
    conn.close()
    logging.info("Products database setup completed.")

def setup_orders_db():
    """Set up the Orders database with foreign key constraints."""
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL CHECK(quantity > 0),
        FOREIGN KEY (user_id) REFERENCES Users(id),
        FOREIGN KEY (product_id) REFERENCES Products(id)
    )""")
    conn.commit()
    conn.close()
    logging.info("Orders database setup completed.")

def setup_databases():
    """Set up all databases."""
    logging.info("Starting database setup.")
    setup_users_db()
    setup_products_db()
    setup_orders_db()
    logging.info("All databases set up successfully.")
