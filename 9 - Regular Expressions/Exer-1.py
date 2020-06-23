import re

pattern = r"\d+"
text = ""

while True:
    line = input()
    if line:
        text += line
    else:
        break

result = re.findall(pattern, text, )
print(" ".join(result))
