from database.connection import get_asigned_task,get_complaint_details,update_complaint
from tabulate import tabulate

def asinged_task():
    
    print("""
          ====================================================
                            Assigned task 
          ====================================================
          
          """)

    emp_int = input("Enter employee id : ")

    result = get_asigned_task(emp_int)

    headers = ["assignment_id", "complaint_id", "employee_id", "assigned_at"]

    if not result:
        print("No assigned complaints to U !!.")
    else:
        print(tabulate(result, headers=headers, tablefmt="grid"))
        asinged_task_details()
    
def asinged_task_details():
    print("""
          ====================================================
                            Assigned task with full details
          ====================================================
          
          """)   
    
    comp_id=int(input("Enter a complaint id : "))
    
    result = get_complaint_details(comp_id=comp_id)
    
    headers = [
        "ticket_id",
        "customer_name",
        "phone number"
        "problem",
        "priority",
        "status",
    ]

    if not result:
        print("No assigned complaints found.")
    else:
        print(tabulate(result, headers=headers, tablefmt="grid"))
        
        
    status = int(input("""
            ================ Work Completed ==============
            1. Open
            2. Close
            ===============================================
            Enter status: """))

    status_set = {
        1: "open",
        2: "close"
    }

    status = status_set.get(status)
    
    update_complaint(comp_id=comp_id,status=status)
