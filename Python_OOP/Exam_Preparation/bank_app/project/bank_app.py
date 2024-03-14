from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOANS:
            raise Exception("Invalid loan type!")
        loan = self.LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client = self.CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))
        client = next(filter(lambda c: c.client_id == client_id, self.clients))

        if loan.TYPE_ != client.TYPE_:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                count += 1
                loan.increase_interest_rate()

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0

        for client in self.clients:
            if client.interest < min_rate:
                count += 1
                client.increase_clients_interest()

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        avg_interest = 0

        if self.clients:
            for client in self.clients:
                avg_interest += client.interest
            avg_interest /= len(self.clients)

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {sum(x.income for x in self.clients):.2f}\n" \
               f"Granted Loans: {sum(len(x.loans) for x in self.clients)}, Total Sum: {sum(sum(x.amount for x in y.loans) for y in self.clients):.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {sum(x.amount for x in self.loans):.2f}\n" \
               f"Average Client Interest Rate: {avg_interest:.2f}"
