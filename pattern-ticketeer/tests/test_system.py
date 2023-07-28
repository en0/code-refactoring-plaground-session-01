import pytest
import ticket as ticket_module


def test_create_ticket():
    ticket = ticket_module.create_ticket("Test Ticket", "This is a test ticket")
    assert ticket.title == "Test Ticket"
    assert ticket.description == "This is a test ticket"
    assert ticket.current_state == "Todo"


def test_delete_ticket():
    ticket = ticket_module.create_ticket("Test Ticket", "This is a test ticket")
    result = ticket_module.delete_ticket(ticket.title)
    assert result is True


def test_update_ticket():
    ticket = ticket_module.create_ticket("Test Ticket", "This is a test ticket")
    result = ticket_module.update_ticket(ticket.title, "Updated Ticket", "This is an updated ticket")
    assert result is True

    updated_ticket = ticket_module.get_ticket_by_title("Updated Ticket")
    assert updated_ticket.title == "Updated Ticket"
    assert updated_ticket.description == "This is an updated ticket"


def test_transition_ticket_state():
    ticket = ticket_module.create_ticket("Test Ticket", "This is a test ticket")
    result = ticket_module.transition_ticket_state(ticket.title, "InProgress")
    assert result is True

    ticket_after_transition = ticket_module.get_ticket_by_title(ticket.title)
    assert ticket_after_transition.current_state == "InProgress"


def test_list_available_states_for_ticket():
    ticket = ticket_module.create_ticket("Test Ticket", "This is a test ticket")
    available_states = ticket_module.list_available_states_for_ticket(ticket.title)
    assert available_states == ["InProgress"]


def test_list_all_possible_states():
    possible_states = ticket_module.list_all_possible_states()
    assert possible_states == ["Todo", "InProgress", "Done"]


def test_list_all_tickets():
    ticket1 = ticket_module.create_ticket("Ticket 1", "This is ticket 1")
    ticket2 = ticket_module.create_ticket("Ticket 2", "This is ticket 2")
    ticket3 = ticket_module.create_ticket("Ticket 3", "This is ticket 3")

    all_tickets = ticket_module.list_all_tickets()
    assert len(all_tickets) == 3
    assert ticket1 in all_tickets
    assert ticket2 in all_tickets
    assert ticket3 in all_tickets

