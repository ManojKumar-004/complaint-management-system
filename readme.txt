# Complaint Management System

A console-based Complaint Management System developed using Python and MySQL.

## Features

- Customer registration
- Employee registration
- Complaint registration
- Complaint assignment
- Complaint status update
- Customer feedback
- Admin feedback view
- Employee feedback view
- Automatic database and table creation

## Technologies

- Python
- MySQL
- mysql-connector-python
- Tabulate

## Project Structure

PYTHON/
│
├── admin/
├── customer/
├── Employee/
│
├── database/
│   ├── connection.py
│   └── create_database.py
│
├── main.py
└── README.md

## Database

Database name:

complaint_system

Tables:

- customer
- employee
- complaint
- assignment
- feedback

## Installation

Install the required packages:

pip install mysql-connector-python tabulate

Make sure MySQL Server is running.

## MySQL Configuration

Update the MySQL details in database/create_database.py:

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123"
)

Change the password according to your MySQL configuration.

## Automatic Database Creation

The project automatically creates the database and tables.

If the database exists:
Use the existing database.

If the database does not exist:
Create the database.

If the table exists:
Use the existing table.

If the table does not exist:
Create the table.

Existing data will not be deleted.

## Run the Project

From the project folder:

python main.py

## Complaint Flow

Customer
↓
Raise Complaint
↓
Admin
↓
Assign Employee
↓
Employee
↓
Complete Complaint
↓
Close Complaint
↓
Customer
↓
Give Feedback
↓
Admin / Employee
↓
View Feedback

## Complaint Priority

1. Low
2. Medium
3. High
4. Critical

## Complaint Status

- open
- close

## Author

Manoj Kumar

## Purpose

This project was created for learning and practicing Python, MySQL, CRUD operations, database relationships, and modular programming.