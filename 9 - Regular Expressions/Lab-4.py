import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()
result = re.finditer(pattern, text)

for match in result:
    print(match.group(0), end=' ')
