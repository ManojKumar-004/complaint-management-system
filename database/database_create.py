import mysql.connector


def create_database():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    cur = connection.cursor()

    # Create database if it does not exist
    cur.execute("""
        CREATE DATABASE IF NOT EXISTS complaint_system
    """)

    connection.database = "complaint_system"

    # Customer
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)

    # Employee
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            employee_id INT PRIMARY KEY,
            employee_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)

    # Complaint
    cur.execute("""
        CREATE TABLE IF NOT EXISTS complaint (
            complaint_id INT AUTO_INCREMENT PRIMARY KEY,
            ticket_id VARCHAR(20) UNIQUE NOT NULL,
            customer_id INT NOT NULL,
            machine_model VARCHAR(100),
            machine_number VARCHAR(100),
            problem TEXT NOT NULL,
            priority VARCHAR(20),
            status VARCHAR(20) DEFAULT 'open',

            FOREIGN KEY (customer_id)
            REFERENCES customer(customer_id)
        )
    """)

    # Assignment
    cur.execute("""
        CREATE TABLE IF NOT EXISTS assignment (
            assignment_id INT AUTO_INCREMENT PRIMARY KEY,
            complaint_id INT NOT NULL,
            employee_id INT NOT NULL,
            assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (complaint_id)
            REFERENCES complaint(complaint_id),

            FOREIGN KEY (employee_id)
            REFERENCES employee(employee_id)
        )
    """)

    # Feedback
    cur.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            feedback_id INT AUTO_INCREMENT PRIMARY KEY,
            complaint_id INT NOT NULL,
            customer_id INT NOT NULL,
            rating INT NOT NULL,
            comments TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (complaint_id)
            REFERENCES complaint(complaint_id),

            FOREIGN KEY (customer_id)
            REFERENCES customer(customer_id)
        )
    """)

    connection.commit()

    cur.close()
    connection.close()