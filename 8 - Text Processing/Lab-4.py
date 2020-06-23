banned_words = input().split(', ')
text = input()

for word in banned_words:
    replace = len(word) * '*'
    text = text.replace(word, replace)

print(text)
