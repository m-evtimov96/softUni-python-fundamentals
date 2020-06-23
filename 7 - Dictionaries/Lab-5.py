num_words = int(input())
synonyms = {}

for _ in range(num_words):
    word = input()
    synonym = input()
    if word in synonyms.keys():
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym in synonyms.items():
    print(f'{word} - {", ".join(synonym)}')
