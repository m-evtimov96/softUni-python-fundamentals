import re

pattern = r"(.+)>(?P<Pass>[\d]{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1"

inputs_num = int(input())

for _ in range(inputs_num):
    password = input()
    match = re.match(pattern, password)

    if match is None:
        print("Try another password!")
    else:
        encrypted_password = match["Pass"]
        encrypted_password = encrypted_password.replace("|", "")
        print(f"Password: {encrypted_password}")
