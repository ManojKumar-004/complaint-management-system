from database.connection import insert_employee,insert_customer,customer_count,employee_count

def add_empcu():
    print("""
              ===================================
                 Add customer / employee  PANEL
              ===================================
          """)
    
    print("""
          
            1.Customer
            2.Employee
            
        """)
    
    admin_in = int(input("Enter Your choices : "))
    
    if admin_in ==1:
        count = customer_count()
        customer_id = count+1 
        customer_name = input("Enter a customer Name : ")
        customer_email = input("Enter a customer Email : ")
        customer_phone = input("Enter a customer Phone ")
        insert_customer(customer_id,customer_name,customer_email,customer_phone)
    elif admin_in ==2:
        count_emp = employee_count()
        employee_id = count_emp +1
        employee_name = input("Enter a employee Name : ")
        employee_email = input("Enter a employee Email : ")
        employee_phone = input("Enter a employee Phone ")
        insert_employee(employee_id,employee_name,employee_email,employee_phone)
    else:
        print("Enter a give option!!")