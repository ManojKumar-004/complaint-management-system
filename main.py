from customer.customer import customer_menu
from admin.admin import admin_menu
from Employee.employee import employee_menu
print(
        '''
        ========================================
                SERVICE COMPLAINT REGISTER
        ========================================
        '''
    )
while True:
    print("""
          1.Customer
          2.Admin
          3.Employee
          4.Exit
          """)
    
    User_input = int(input("Enter you choice : "))
    
    if User_input == 1:
        customer_menu()
    elif User_input == 2:
        admin_menu()
    elif User_input == 3:
        employee_menu()
    elif User_input == 4:
        print("\n  ------ Thank you welcome back ------ ")
        quit()
    else :
        print("\n **** Chosee a corret option given above ****") 
    