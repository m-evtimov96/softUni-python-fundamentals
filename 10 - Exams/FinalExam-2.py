import re

pattern = r"((::|\*\*)[A-Z][a-z]{2,}\2)"

text = input()
cool_threshold = 1

for char in text:
    if char.isdigit():
        cool_threshold *= int(char)

emojis = [groups[0] for groups in re.findall(pattern, text)]

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")

for emoji in emojis:
    coolness = sum([ord(char) for char in emoji if char != ":" and char != "*"])
    if coolness > cool_threshold:
        print(emoji)
