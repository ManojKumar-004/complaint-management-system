from .Assigned_task import *
from .view_feed_back import view_feedback
def employee_menu():
    print("""
          
          =================================================
                        Employee Menu 
          =================================================
          
          1.Assigned complaint
          2.View Feed back
          """)

    emp_input = int(input("Enter your option : "))

    if emp_input ==1:
        asinged_task()
    elif emp_input == 2:
        view_feedback()
    else:
        print("enter correct option!!!!")
