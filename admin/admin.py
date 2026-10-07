from admin.add_cus_emp import add_empcu
from admin.asign_task import assigning_task
from .feedback import view_feedback
def admin_menu():

    while True:
        print("""
              ===================================
                        ADMIN PANEL
              ===================================
              """)
        
        print("""
              
              1.Add customer/employee
              2.Assing task             
              3.view feed back
              4.Back
              """)
        
        admin_choss = int(input("Enter you choice :"))
        
        if admin_choss == 1:
            add_empcu()
        elif admin_choss == 3:
            view_feedback()
        elif admin_choss == 2:
            assigning_task()
        elif admin_choss == 4:
            print("\n")
            print("------------------- Thank admin welcome back ---------------------- ")
            return
        else:
            print("Enter a give option !!")