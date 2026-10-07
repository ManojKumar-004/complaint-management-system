import mysql.connector
from database.database_create import create_database


# Create database/tables if needed
create_database()

connection = mysql.connector.connect(
    host="localhost", # host name 
    user="root",    # user name from you mysql
    password="password", #
    database="your-database-name"
)


# -------------------------------------------------------------------------------------------------
cur = connection.cursor()
# ----------------------------------------------------------------------------

def get_customer_id(name):
    query = "SELECT customer_id FROM customer WHERE customer_name = %s"

    cur.execute(query, (name,))

    customer_id = cur.fetchone()

    return customer_id[0]


def complaint_count():
    query = "SELECT COUNT(*) FROM complaint"

    cur.execute(query)

    result = cur.fetchone()

    return result[0]


def inser_complaint(
    ticket_id,
    customer_id,
    machine_model,
    machine_number,
    problem,
    priority,
    status
):

    query = """
    INSERT INTO complaint
    (ticket_id, customer_id, machine_model, machine_number,
     problem, priority, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        ticket_id,
        customer_id,
        machine_model,
        machine_number,
        problem,
        priority,
        status
    )

    cur.execute(query, values)

    connection.commit()

    print("\n--------------- Complaint registered successfully ------------------")
    
    
def insert_customer(
    customer_id,
    customer_name,
    customer_email,
    customer_phone
):

    query = """
    INSERT INTO customer
    (customer_id,customer_name, email, phone)
    VALUES (%s, %s, %s,%s)
    """

    values = (
    customer_id,
    customer_name,
    customer_email,
    customer_phone
    )

    cur.execute(query, values)

    connection.commit()

    print("\n--------------- Customer details registered successfully ------------------")
    
    
def insert_employee(
    employee_id,
    employee_name,
    employee_email,
    employee_phone
):

    query = """
    INSERT INTO employee
    (employee_id,employee_name, email, phone)
    VALUES (%s, %s, %s,%s)
    """

    values = (
    employee_id,
    employee_name,
    employee_email,
    employee_phone
    )

    cur.execute(query, values)

    connection.commit()

    print("\n--------------- Employee details registered successfully ------------------")


def employee_count():
    query = "SELECT COUNT(*) FROM employee"

    cur.execute(query)

    result = cur.fetchone()

    return result[0]

def customer_count():
    query = "SELECT COUNT(*) FROM customer"

    cur.execute(query)

    result = cur.fetchone()

    return result[0]


def open_complaint(query):
    
    cur.execute(query)
    
    result = cur.fetchall()
    
    return result

def employee_list(query):
    
    cur.execute(query)
    
    result = cur.fetchall()
    
    return result

def assign_complaint_engg(complaint_id, employee_id):

    query = """
        INSERT INTO assignment
        (complaint_id, employee_id)
        VALUES (%s, %s)
    """

    values = (
        complaint_id,
        employee_id
    )

    cur.execute(query, values)

    connection.commit()

    print("\n--------------- Complaint assigned to engineer successfully ------------------")


def get_asigned_task(emp_int):

    try:
        query = '''
            SELECT *
            FROM assignment
            WHERE employee_id = %s
        '''

        cur.execute(query, (emp_int,))

        result = cur.fetchall()

        return result

    except Exception as e:
        return "Employee not found"
    

def get_complaint_details(comp_id):

    try:
        query = '''
            SELECT complaint.ticket_id,
                   customer.customer_name,
                   customer.phone,
                   complaint.problem,
                   complaint.priority,
                   complaint.status
            FROM complaint
            JOIN customer
            ON complaint.customer_id = customer.customer_id
            WHERE complaint.complaint_id = %s
        '''

        cur.execute(query, (comp_id,))

        result = cur.fetchall()

        return result

    except Exception as e:
        return []
    
    
def update_complaint(comp_id, status):

    query = '''
        UPDATE complaint
        SET status = %s
        WHERE complaint_id = %s
    '''

    values = (
        status,
        comp_id
    )

    cur.execute(query, values)
    connection.commit()

    return "Complaint updated successfully"



def get_closed_complaints(customer_id):

    query = """
        SELECT complaint_id, ticket_id, problem, priority, status
        FROM complaint
        WHERE customer_id = %s
        AND status = 'close'
    """

    cur.execute(query, (customer_id,))

    result = cur.fetchall()

    return result


def insert_feedback(complaint_id, customer_id, rating, comments):

    query = """
        INSERT INTO feedback
        (complaint_id, customer_id, rating, comments)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        complaint_id,
        customer_id,
        rating,
        comments
    )

    cur.execute(query, values)

    connection.commit()
    
    
def get_complaints_with_status():

    query = """
        SELECT
            complaint.complaint_id,
            complaint.ticket_id,
            customer.customer_name,
            complaint.problem,
            complaint.priority,
            complaint.status
        FROM complaint
        JOIN customer
        ON complaint.customer_id = customer.customer_id
    """

    cur.execute(query)

    return cur.fetchall()


def get_complaint_feedback(complaint_id):

    query = """
        SELECT
            feedback.feedback_id,
            complaint.ticket_id,
            customer.customer_name,
            feedback.rating,
            feedback.comments,
            feedback.created_at
        FROM feedback
        JOIN complaint
        ON feedback.complaint_id = complaint.complaint_id
        JOIN customer
        ON feedback.customer_id = customer.customer_id
        WHERE feedback.complaint_id = %s
    """

    cur.execute(query, (complaint_id,))

    return cur.fetchall()