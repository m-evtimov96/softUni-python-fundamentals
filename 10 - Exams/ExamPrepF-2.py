import re

pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([a-zA-Z]{5,}\d+)P@\$"
count = int(input())
valid_reg = 0

for i in range(count):
    registration = input()
    match = re.match(pattern, registration)

    if match is None:
        print("Invalid username or password")
    else:
        valid_reg += 1
        print("Registration was successful")
        print(f"Username: {match[1]}, Password: {match[2]}")

print(f"Successful registrations: {valid_reg}")
