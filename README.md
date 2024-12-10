
# SQLite Database Setup and Data Insertion

This project demonstrates how to set up and manage three SQLite databases (`Users`, `Products`, and `Orders`), along with concurrent data insertion using Python's threading module. The project also includes proper validation, logging, and foreign key constraints to ensure data integrity.

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Logging](#logging)

## Features
- **Database Setup**: Create `Users`, `Products`, and `Orders` databases with proper schema and constraints.
- **Validation**: Ensures data integrity with checks for valid users, products, and orders.
- **Concurrency**: Uses Python's threading module for concurrent data insertion.
- **Logging**: Tracks all major operations in a `system.log` file.

## Prerequisites
- Python 3.7+
- SQLite

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/trijal18/sqlite-dev
   ```
2. Navigate to the project directory:
   ```bash
   cd sqlite-setup-project
   ```
3. Install required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to insert data concurrently:
   ```bash
   python main.py
   ```

## Project Structure
```
├── main.py               # Main script to set up databases and insert data
├── setup_databases.py    # Database setup functions
├── data_insertion.py     # Data insertion functions
├── data_validation.py    # Validation logic for data integrity
├── data.py               # Sample data for users, products, and orders
├── system.log            # Log file for tracking operations
└── README.md             # Project documentation
```

## Logging
All major operations are logged to `system.log` with timestamps, including:
- Database creation events
- Data insertion success and errors
- Validation failures
