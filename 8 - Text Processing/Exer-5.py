text = input()

for pos, char in enumerate(text):
    if char == ':':
        emoticon = char + text[pos+1]
        print(emoticon)
