import re

pattern = r"\b_([a-z|A-Z|0-9]+\b)"
text = input()

result = re.findall(pattern, text)
print(",".join(result))
