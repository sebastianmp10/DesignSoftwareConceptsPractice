import string
import random
from typing import List

def generate_id(length=8):
    #helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class SoporteTiquete:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class SoporteCliente:

    tickets: List[SoporteTiquete] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SoporteTiquete(customer, issue))

    def process_tickets(self, processing_strategy: str = "fifo"):
        #if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        if processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
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
app.process_tickets("filo")




