import sqlite3
from data_validation import validate_user, validate_product, validate_order
from data import users_data, products_data, orders_data

def insert_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    for user in users_data:
        if validate_user(user):
            try:
                cursor.execute("INSERT INTO Users (id, name, email) VALUES (?, ?, ?)", user)
            except sqlite3.IntegrityError as e:
                print(f"Users Insert Error: {user} -> {e}")
    conn.commit()
    conn.close()

def insert_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    for product in products_data:
        if validate_product(product):
            try:
                cursor.execute("INSERT INTO Products (id, name, price) VALUES (?, ?, ?)", product)
            except sqlite3.IntegrityError as e:
                print(f"Products Insert Error: {product} -> {e}")
    conn.commit()
    conn.close()

def insert_orders():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    for order in orders_data:
        if validate_order(order):
            try:
                cursor.execute("INSERT INTO Orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)", order)
            except sqlite3.IntegrityError as e:
                print(f"Orders Insert Error: {order} -> {e}")
    conn.commit()
    conn.close()
