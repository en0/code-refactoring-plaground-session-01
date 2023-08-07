from typing import List, Union, Dict
from ticket_management.model import Ticket

class TicketService:
    """
    TicketService is responsible for managing tickets in the PatternTicketeer
    application.
    """

    _tickets: Dict[str, Ticket]
    _initial_state = "Todo"
    _state_map = {
        "Todo": ["InProgress"],
        "InProgress": ["Done"],
        "Done": [],
    }

    def __init__(self) -> None:
        self._tickets = {}

    def create_ticket(self, title: str, description: str) -> Ticket:
        """
        Create a new ticket with the provided title and description.

        Args:
            title (str): The title of the ticket.
            description (str): The description of the ticket.
            initial_state (str): The initial state of the ticket.

        Returns:
            Ticket: The created Ticket object.
        """
        ticket = Ticket(title, description, self._initial_state)
        self._tickets[title] = ticket
        return ticket

    def delete_ticket(self, title: str) -> bool:
        """
        Delete the ticket with the given title

        Args:
            title (str): The unique title of the ticket to be deleted.

        Returns:
            bool: True if the ticket is successfully deleted, False otherwise.
        """
        ticket = self._tickets.get(title)
        if ticket:
            del self._tickets[ticket.title]
            return True
        return False

    def update_ticket(self, title: str, new_title: str, new_description: str) -> bool:
        """
        Update the title and description of the ticket with the given title.

        Args:
            title (str): The unique title of the ticket to be updated.
            new_title (str): The new title for the ticket
            new_description (str): The new description of the ticket.

        Returns:
            bool: True if the ticket is successfully updated, False otherwise.
        """
        ticket = self._tickets.get(title)
        if ticket:
            ticket.description = new_description
            if title != new_title:
                del self._tickets[title]
                ticket.title = new_title
                self._tickets[new_title] = ticket
            return True
        return False

    def transition_ticket_state(self, title: str, new_state: str) -> bool:
        """
        Transition the state of the ticket with the given title to the new_state.

        Args:
            title (str): The unique title of the ticket to be transitioned.
            new_state (str): The new state to which the ticket should be transitioned.

        Returns:
            bool: True if the ticket state is successfully transitioned, False otherwise.
        """
        ticket = self._tickets.get(title)
        if not ticket:
            return False
        if new_state in self._state_map[ticket.current_state]:
            ticket.current_state = new_state
            return True
        return False

    def list_available_states_for_ticket(self, title: str) -> List[str]:
        """
        List the available states that the ticket with the given title can transition to.

        Args:
            title (str): The unique title of the ticket for which available states are to be listed.

        Returns:
            List[str]: A list of available states for the ticket.
        """
        ticket = self._tickets.get(title)
        if ticket:
            return self._state_map[ticket.current_state]
        return []

    def list_all_possible_states(self) -> List[str]:
        """
        List all the possible states.

        Returns:
            List[str]: A list of possible states.
        """
        return list(self._state_map.keys())

    def get_ticket_by_title(self, title: str) -> Union[Ticket, None]:
        """
        Get the ticket with the given title

        Returns:
            Ticket: If the ticket exists, the ticket is returned. Else, None.
        """
        return self._tickets.get(title)

    def list_all_tickets(self) -> List[Ticket]:
        """
        List all existing tickets in the system.

        Returns:
            List[Ticket]: A list of all tickets in the system.
        """
        return list(self._tickets.values())
