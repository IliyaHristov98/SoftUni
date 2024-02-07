class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_emails = []
while True:
    command = input()
    if command == 'Stop':
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    list_of_emails.append(email)
indexes = [int(index) for index in input().split(", ")]
for x in indexes:
    list_of_emails[x].send()
for y in list_of_emails:
    print(y.get_info())
