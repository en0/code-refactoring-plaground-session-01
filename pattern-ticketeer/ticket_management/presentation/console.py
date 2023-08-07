from ticket_management.model import Ticket
from ticket_management.service.ticket_service import TicketService


def display_tickets(tickets):
    if not tickets:
        print("No tickets found.")
        return
    for index, ticket in enumerate(tickets, 1):
        print(f"{index}. {ticket.title} - {ticket.current_state}")


def display_ticket(ticket):
    if not ticket:
        print("No ticket found.")
    else:
        print(f"{ticket.title} - {ticket.current_state}")
        print(ticket.description)


def main():
    ticket_service = TicketService()

    while True:
        print("\n=== PatternTicketeer - Command Line Interface ===")
        print("1. Create New Ticket")
        print("2. Delete Ticket")
        print("3. Update Ticket Title and Description")
        print("4. Transition Ticket State")
        print("5. List Available States for Ticket")
        print("6. List All Possible States")
        print("7. List All Tickets")
        print("8. Get Ticket by Title")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            title = input("Enter the title of the ticket: ")
            description = input("Enter the description of the ticket: ")
            ticket = ticket_service.create_ticket(title, description)
            print(f"Ticket '{ticket.title}' created successfully!")

        elif choice == "2":
            title = input("Enter the title of the ticket to delete: ")
            if ticket_service.delete_ticket(title):
                print(f"Ticket '{title}' deleted successfully!")
            else:
                print(f"Ticket '{title}' not found!")

        elif choice == "3":
            title = input("Enter the title of the ticket to update: ")
            new_title = input("Enter the new title for the ticket: ")
            new_description = input("Enter the new description for the ticket: ")
            if ticket_service.update_ticket(title, new_title, new_description):
                print(f"Ticket '{title}' updated successfully!")
            else:
                print(f"Ticket '{title}' not found!")

        elif choice == "4":
            title = input("Enter the title of the ticket to transition: ")
            new_state = input("Enter the new state for the ticket: ")
            if ticket_service.transition_ticket_state(title, new_state):
                print(f"Ticket '{title}' state transitioned successfully!")
            else:
                print(f"Ticket '{title}' not found or invalid state transition!")

        elif choice == "5":
            title = input("Enter the title of the ticket to list available states: ")
            available_states = ticket_service.list_available_states_for_ticket(title)
            print(f"Available states for ticket '{title}': {', '.join(available_states)}")

        elif choice == "6":
            all_states = ticket_service.list_all_possible_states()
            print("All possible states:", ', '.join(all_states))

        elif choice == "7":
            tickets = ticket_service.list_all_tickets()
            display_tickets(tickets)

        elif choice == "8":
            title = input("Enter the title of the ticket to get: ")
            ticket = ticket_service.get_ticket_by_title(title)
            display_ticket(ticket)

        elif choice == "9":
            print("Exiting PatternTicketeer - Command Line Interface")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
