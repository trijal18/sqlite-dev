import threading
from database_setup import setup_databases
from data_insertion import insert_users, insert_products, insert_orders

def main():
    # Setup databases
    setup_databases()

    # Create threads for concurrent insertion
    threads = [
        threading.Thread(target=insert_users),
        threading.Thread(target=insert_products),
        threading.Thread(target=insert_orders),
    ]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Insertion complete.")

if __name__ == "__main__":
    main()
