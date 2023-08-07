from dataclasses import dataclass

@dataclass
class Ticket:
    title: str
    description: str
    current_state: str
