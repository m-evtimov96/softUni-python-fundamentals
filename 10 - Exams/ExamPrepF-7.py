username = input()

while True:
    input_line = input()
    if input_line == "Sign up":
        break
    input_line = input_line.split()
    command = input_line[0]

    if command == "Case":
        case_type = input_line[1]
        if case_type == "lower":
            username = username.lower()
        elif case_type == "upper":
            username = username.upper()
        print(username)
    elif command == "Reverse":
        start = int(input_line[1])
        end = int(input_line[2])
        if 0 <= start <= len(username) and 0 <= end <= len(username) and end > start:
            print("".join(reversed(username[start:end+1])))
    elif command == "Cut":
        string_to_check = input_line[1]
        if string_to_check in username:
            username = username.replace(string_to_check, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {string_to_check}.")
    elif command == "Replace":
        char_to_replace = input_line[1]
        username = username.replace(char_to_replace, "*")
        print(username)
    elif command == "Check":
        char_to_check = input_line[1]
        if char_to_check in username:
            print("Valid")
        else:
            print(f"Your username must contain {char_to_check}.")
