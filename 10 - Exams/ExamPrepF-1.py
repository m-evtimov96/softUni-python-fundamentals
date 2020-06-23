email = input()

while True:
    text_input = input()
    if text_input == "Complete":
        break

    input_line = text_input.split()
    command = input_line[0]

    if text_input == "Make Upper":
        email = email.upper()
        print(email)
    elif text_input == "Make Lower":
        email = email.lower()
        print(email)
    elif command == "GetDomain":
        count = int(input_line[1])
        domain = email[-count:]
        print(domain)
    elif command == "GetUsername":
        index = email.find("@")
        if index == -1:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            print(email[:index])
    elif command == "Replace":
        char = input_line[1]
        email = email.replace(char, "-")
        print(email)
    elif text_input == "Encrypt":
        for ch in email:
            print(ord(ch), end=" ")
