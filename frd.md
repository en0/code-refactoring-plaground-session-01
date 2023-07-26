# Code Refactoring Playground - Session 1 FRD

## 1. Introduction:

PatternTicketeer is an in-memory ticket management application accessible
through a command-line interface. The system allows users to create, manage, and
track tickets. This Feature Requirements Document outlines the key
functionalities and interactions for the PatternTicketeer application.

## 2. Domain Objects:

- **Ticket:** Represents a ticket within the system.
  - Title: A unique title for the ticket (must be unique among all tickets).
  - Description: A detailed explanation of the ticket.
  - Current State: The current state of the ticket. Can be one of the following:
    `Todo`, `InProgress`, or `Done`.

## 3. Actors:

- **User:** The primary actor who interacts with the system to manage tickets.
  - Actions: Create new tickets, delete existing tickets, update ticket title
    and description, transition tickets to allowed states, list available states
    for a ticket, and list all possible states for a ticket, list all tickets.

## 4. Functional Requirements:

The following functionalities describe the actions that users can perform within
the PatternTicketeer application:

- **Create New Ticket:**
  - Description: Users can create new tickets with a unique title, description,
    and initial state of `Todo`.
  - Input: Title and description.
  - Output: Confirmation message for successful creation.

- **Delete Ticket:**
  - Description: Users can delete an existing ticket from the system.
  - Input: Ticket title to be deleted.
  - Output: Confirmation message for successful deletion.

- **Update Ticket Title and Description:**
  - Description: Users can update the title and description of an existing
    ticket.
  - Input: Ticket title and the new title/description.
  - Output: Confirmation message for successful update.

- **Transition Ticket State:**
  - Description: Users can transition a ticket to an allowed state.
  - Input: Ticket title and the desired new state.
  - Output: Confirmation message for successful state transition.

- **List Available States for Ticket:**
  - Description: Users can view the available states that a ticket can transition to.
  - Input: Ticket title.
  - Output: List of available states based on the current state.

- **List All Possible States for Ticket:**
  - Description: Users can view all the possible states for a ticket.
  - Output: List of possible states.

- **Get Ticket by Title:**
  - Description: Users can retrieve a single ticket by the ticket title.
  - input: Ticket title.
  - Output: The ticket with the same title or none if the ticket doesn't exist.

- **List All Tickets:**
  - Description: Users can view a list of all existing tickets in the system.
  - Output: A list of all tickets, including their titles, current states.

## 5. Non-Functional Requirements:

- User inputs and outputs should be intuitive and user-friendly through the
  command-line interface.
- The application should maintain data integrity and consistency while managing
  tickets.

## 6. Assumptions:

- User authentication is not required for the current implementation.
- The application will store data in-memory during runtime. Data will not persist between runs.

## 7. Constraints:

- The command-line interface will be the only means of interacting with the
  application.

- State Transitions:
  - Initial State: All new tickets are created with the state `Todo`.
  - Final State: The state `Done` is a final state and cannot be changed.
  - Valid state transitions:
    - `Todo` -> `InProgress`
    - `InProgress` -> `Done`

## 8. Future Scope:

- Implementation of additional features and enhancements, such as TicketTypes
  and associated workflows, to support various ticket scenarios.
- Integration with an external database for persistent data storage.
- Handling concurrent users for future scalability.
- User authentication for enhanced security and access control.

## 9. Conclusion:

PatternTicketeer provides an interactive and efficient platform for users to
manage tickets. With its command-line interface and intuitive functionalities,
PatternTicketeer empowers users to refine their code, leverage design patterns,
and become adept at the art of refactoring.

