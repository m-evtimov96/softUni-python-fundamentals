def is_valid(password):
    valid = True
    wrong_char = False
    digits = 0
    if not 6 <= len(password) <= 10:
        valid = False
        print('Password must be between 6 and 10 characters')
    for char in password:
        if not 48 <= ord(char) <= 57 and not 65 <= ord(char) <= 90 and not 97 <= ord(char) <= 122:
            wrong_char = True
        if 48 <= ord(char) <= 57:
            digits += 1
    if wrong_char:
        valid = False
        print('Password must consist only of letters and digits')
    if digits < 2:
        valid = False
        print('Password must have at least 2 digits')

    if valid:
        print('Password is valid')


password1 = input()
is_valid(password1)
