from complaints.Complaint import complaint_reg
from .give_feedback import *


def customer_menu():
    print(
        '''
        ========================================
                    CUSTOMER PANEL
        ========================================
        
        '''    
    )
    
    while True:
        print(
            """
            1. Register Complaint
            2. Give Feedback
            3. Back
            """
        )
        
        customer_input = int(input("Enter you chosee : "))

        if customer_input == 1:
            complaint_reg()
        elif customer_input == 2:
            give_feedback()
        elif customer_input == 3:
            print("\n  ------ Thank you customer  ------ ")
            return
        else :
            print("\n **** Chosee a corret option given above ****") 
        