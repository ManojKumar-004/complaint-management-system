from database.connection import (
    get_complaints_with_status,
    get_complaint_feedback
)

from tabulate import tabulate


def view_feedback():

    result = get_complaints_with_status()

    headers = [
        "Complaint ID",
        "Ticket ID",
        "Customer",
        "Problem",
        "Priority",
        "Status"
    ]

    if not result:
        print("\nNo complaints found.")
        return

    print("\n================ Complaints ================\n")

    print(tabulate(result, headers=headers, tablefmt="grid"))

    comp_id = int(
        input("\nEnter complaint ID to view feedback : ")
    )

    # Find selected complaint
    selected = None

    for complaint in result:
        if complaint[0] == comp_id:
            selected = complaint
            break

    if not selected:
        print("Complaint not found.")
        return

    # status is index 5
    if selected[5] != "close":
        print("\nThis complaint is still OPEN.")
        print("Feedback is available only for closed complaints.")
        return

    feedback = get_complaint_feedback(comp_id)

    if not feedback:
        print("\nNo feedback given by customer.")
        return

    feedback_headers = [
        "Feedback ID",
        "Ticket ID",
        "Customer",
        "Rating",
        "Comments",
        "Created At"
    ]

    print("\n================ Customer Feedback ================\n")

    print(
        tabulate(
            feedback,
            headers=feedback_headers,
            tablefmt="grid"
        )
    )