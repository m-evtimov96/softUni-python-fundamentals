import re

pattern = r"( |^)[0-9a-z]+([\.\-_][0-9a-z]+)*@[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"
text = input()

mails = re.finditer(pattern, text)

for mail in mails:
    mail_print = mail[0].strip()
    print(mail_print)
