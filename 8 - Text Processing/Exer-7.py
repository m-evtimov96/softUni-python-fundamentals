text = input()
explosions = 0
i = 0

while i < len(text):
    char = text[i]

    if char == '>':
        explosions += int(text[i + 1])
    elif explosions > 0:
        text = text[:i] + text[i + 1:]
        i -= 1
        explosions -= 1
    i += 1

print(text)
