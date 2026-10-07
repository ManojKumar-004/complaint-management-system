from database.connection import inser_complaint,complaint_count,get_customer_id

def complaint_reg():
    print(
        '''
        ========================================
                   REGISTER COMPLAINT
        ========================================
        
        '''
    )
    print("  ------- fill up the form -------")
    Customer_Name = input("Enter you Company name : ")
    Phone_Number = input("Enter you Phone number : ")
    #Email = input("Enter you email :  ")
    Machine_model=input("Enter you machine model  :  ")
    Machine_number = input("Enter you machine number :  ")
    
    problem = input("Enter you problem :  ")
    
    priority_choice = int(input(
    '''
    Priority :
            1. low
            2. medium
            3. high
            4. critical
    '''
    ))

    priority = {
        1: "low",
        2: "medium",
        3: "high",
        4: "critical"
    }

    problem_priority = priority[priority_choice]

    def generate_ticket():
        tic_prifix = "CMP"
        count = complaint_count()
        tic_count = 1 + count
        ticket_token = tic_prifix + str(tic_count).zfill(3)
        return ticket_token
    
    status = "open"
    
    print()
    print(""""\n
          ========================================
                 COMPLAINT REGISTERED
          ========================================
          """)
    ticket_id = generate_ticket()
    print(f"Ticket id : {ticket_id}")
    print(f"Customer name : {Customer_Name}")
    print(f"Customer number : {Phone_Number}")
    print(f"Machine model : {Machine_model}")
    print(f"Machine number: {Machine_number}")
    print(f"Problem       : {problem}")
    print(f"Priority      : {problem_priority}")
    print(f"status        : {status}")
    print("Our engineer will be assigned shortly.")
    print("========================================")
    customer_id = get_customer_id(Customer_Name)
    inser_complaint(ticket_id,customer_id,Machine_model,Machine_number,problem,problem_priority,status)
    