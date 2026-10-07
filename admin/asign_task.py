from database.connection import open_complaint,employee_list,assign_complaint_engg
from tabulate import tabulate

def assigning_task():
    
    print("""
            New Task :-
          """)


    qurey = '''

        SELECT complaint.complaint_id,complaint.ticket_id, complaint.status, customer.customer_name,customer.email,customer.phone
        FROM complaint
        JOIN customer
        ON complaint.customer_id = customer.customer_id
        WHERE complaint.status = 'open'; 
    
    '''
    
    Result = open_complaint(query=qurey)
    
    # print(Result)

    print("Complaint open list :-")
    headers = ["Complaint ID","Ticket ID", "Status", "Customer Name", "Email", "Phone"]
    print(tabulate(Result, headers=headers, tablefmt="grid"))
    
    print()
    print("Engg list :-")
    query= "select employee_id,employee_name from employee;"
    Result=employee_list(query)
    headers = ["Employee ID","Employee Name"]
    print(tabulate(Result, headers=headers, tablefmt="grid"))
    
    complaint_id_asing = int(input("Enter a complaint_id  number to assign to engg : "))
    employee_id_asing = int(input("Enter a employee_id  number to assign the complaint : "))
    
    
    assign_complaint_engg(complaint_id=complaint_id_asing,employee_id=employee_id_asing)