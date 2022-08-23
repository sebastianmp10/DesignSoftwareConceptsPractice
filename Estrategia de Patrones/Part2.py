import string
import random
from typing import List
from abc import ABC, abstractmethod

class SoporteTiquete:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

def generate_id(length=8):
    #helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        return list.copy()

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy

class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        return []

class SoporteCliente:

    tickets: List[SoporteTiquete] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SoporteTiquete(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        # create the ordered list
        ticket_list = processing_strategy.create_ordering(self.tickets)

        #if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)


    def process_ticket(self, ticket: SoporteTiquete):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Cliente: {ticket.customer}")
        print(f"Problema: {ticket.issue}")
        print("==================================")

#create the application
app = SoporteCliente()

# register a few tickets
app.create_ticket("John Smith", "Mi computador hace sonidos raros!")
app.create_ticket("Linus Sebastian", "No puedo subir videos, ayuda")
app.create_ticket("Arjan Egges", "VSCode no resuelve los bugs automaticamente")

#process the tickets
app.process_tickets(RandomOrderingStrategy())