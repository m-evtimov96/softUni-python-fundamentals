class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    command = input()
    if command == 'Stop':
        break
    email_in = command.split(' ')
    email = Email(email_in[0], email_in[1], email_in[2])
    emails.append(email)

send_emails = list(map(int, input().split(', ', maxsplit=2)))

for el in send_emails:
    emails[el].send()

for email in emails:
    print(email.get_info())
