users = {}

while True:
    text_input = input()
    if text_input == "Statistics":
        break

    text_input = text_input.split("->")
    command = text_input[0]
    username = text_input[1]

    if command == "Add":
        if username in users:
            print(f"{username} is already registered")
        else:
            users[username] = []
    elif command == "Send":
        users[username].append(text_input[2])
    elif command == "Delete":
        if username in users:
            users.pop(username)
        else:
            print(f"{username} not found!")

users = dict(sorted(users.items(), key=lambda u: (-len(u[1]), u[0])))

print(f"Users count: {len(users)}")
for user, emails in users.items():
    print(user)

    for email in emails:
        print(f" - {email}")
