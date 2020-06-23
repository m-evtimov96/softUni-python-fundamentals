def check_username(username):
    for char in username:
        if not char.isdigit() and not char.isalpha() and char != '-' and char != '_':
            return False
    return True


def validate_username(username):
    if 3 <= len(username) <= 16 and check_username(username):
        return username


usernames = input().split(', ')
valid_usernames = list(filter(validate_username, usernames))
print('\n'.join(valid_usernames))

