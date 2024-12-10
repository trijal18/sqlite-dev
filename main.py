import logging
import threading
from database_setup import setup_databases
from data_insertion import insert_users, insert_products, insert_orders

# Configure logging
logging.basicConfig(
    filename="system.log",
    filemode="a",  # Append to the log file
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    logging.info("Starting database setup.")
    # Setup databases
    setup_databases()

    # Create threads for concurrent insertion
    threads = [
        threading.Thread(target=insert_users),
        threading.Thread(target=insert_products),
        threading.Thread(target=insert_orders),
    ]

    logging.info("Starting threads for data insertion.")
    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    logging.info("Data insertion completed.")
    print("Insertion complete.")

if __name__ == "__main__":
    main()
