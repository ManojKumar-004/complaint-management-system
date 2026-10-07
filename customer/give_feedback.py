from database.connection import (
    get_customer_id,
    get_closed_complaints,
    insert_feedback
)

from tabulate import tabulate


def give_feedback():

    customer_name = input("Enter your name : ")

    customer_id = get_customer_id(customer_name)

    if not customer_id:
        print("Customer not found.")
        return

    complaints = get_closed_complaints(customer_id)

    if not complaints:
        print("\nYou don't have any completed complaints.")
        return

    headers = [
        "Complaint ID",
        "Ticket ID",
        "Problem",
        "Priority",
        "Status"
    ]

    print("\n================ Completed Complaints ================\n")

    print(
        tabulate(
            complaints,
            headers=headers,
            tablefmt="grid"
        )
    )

    complaint_id = int(
        input("\nEnter complaint ID to give feedback : ")
    )

    rating = int(
        input("Enter rating (1-5) : ")
    )

    comments = input("Enter your comments : ")

    insert_feedback(
        complaint_id,
        customer_id,
        rating,
        comments
    )

    print("\nFeedback submitted successfully.")