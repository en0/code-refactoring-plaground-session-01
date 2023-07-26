from typing import List, Union
from dataclasses import dataclass


@dataclass
class Ticket:
    title: str
    description: str
    current_state: str


def create_ticket(title: str, description: str) -> Ticket:
    """
    Create a new ticket with the provided title and description.

    Args:
        title (str): The title of the ticket.
        description (str): The description of the ticket.
        initial_state (str): The initial state of the ticket.

    Returns:
        Ticket: The created Ticket object.
    """
    pass


def delete_ticket(title: str) -> bool:
    """
    Delete the ticket with the given title

    Args:
        title (str): The unique title of the ticket to be deleted.

    Returns:
        bool: True if the ticket is successfully deleted, False otherwise.
    """
    pass


def update_ticket(title: str, new_title: str, new_description: str) -> bool:
    """
    Update the title and description of the ticket with the given title.

    Args:
        title (str): The unique title of the ticket to be updated.
        new_title (str): The new title for the ticket
        new_description (str): The new description of the ticket.

    Returns:
        bool: True if the ticket is successfully updated, False otherwise.
    """
    pass


def transition_ticket_state(title: str, new_state: str) -> bool:
    """
    Transition the state of the ticket with the given title to the new_state.

    Args:
        title (str): The unique title of the ticket to be transitioned.
        new_state (str): The new state to which the ticket should be transitioned.

    Returns:
        bool: True if the ticket state is successfully transitioned, False otherwise.
    """
    pass


def list_available_states_for_ticket(title: str) -> List[str]:
    """
    List the available states that the ticket with the given title can transition to.

    Args:
        title (str): The unique title of the ticket for which available states are to be listed.

    Returns:
        List[str]: A list of available states for the ticket.
    """
    pass


def list_all_possible_states() -> List[str]:
    """
    List all the possible states.

    Returns:
        List[str]: A list of possible states.
    """
    pass


def get_ticket_by_title(title: str) -> Union[Ticket, None]:
    """
    Get the ticket with the given title

    Returns:
        Ticket: If the ticket exists, the ticket is returned. Else, None.
    """
    pass


def list_all_tickets() -> List[Ticket]:
    """
    List all existing tickets in the system.

    Returns:
        List[Ticket]: A list of all tickets in the system.
    """
    pass


def main():

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
            ticket = create_ticket(title, description)
            print(f"Ticket '{ticket.title}' created successfully!")

        elif choice == "2":
            title = input("Enter the title of the ticket to delete: ")
            if delete_ticket(title):
                print(f"Ticket '{title}' deleted successfully!")
            else:
                print(f"Ticket '{title}' not found!")

        elif choice == "3":
            title = input("Enter the title of the ticket to update: ")
            new_title = input("Enter the new title for the ticket: ")
            new_description = input("Enter the new description for the ticket: ")
            if update_ticket(title, new_title, new_description):
                print(f"Ticket '{title}' updated successfully!")
            else:
                print(f"Ticket '{title}' not found!")

        elif choice == "4":
            title = input("Enter the title of the ticket to transition: ")
            new_state = input("Enter the new state for the ticket: ")
            if transition_ticket_state(title, new_state):
                print(f"Ticket '{title}' state transitioned successfully!")
            else:
                print(f"Ticket '{title}' not found or invalid state transition!")

        elif choice == "5":
            title = input("Enter the title of the ticket to list available states: ")
            available_states = list_available_states_for_ticket(title)
            print(f"Available states for ticket '{title}': {', '.join(available_states)}")

        elif choice == "6":
            all_states = list_all_possible_states()
            print("All possible states:", ', '.join(all_states))

        elif choice == "7":
            tickets = list_all_tickets()
            display_tickets(tickets)

        elif choice == "8":
            title = input("Enter the title of the ticket to get: ")
            ticket = get_ticket_by_title(title)
            display_ticket(ticket)

        elif choice == "9":
            print("Exiting PatternTicketeer - Command Line Interface")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
