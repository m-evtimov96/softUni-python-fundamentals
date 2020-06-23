cycles = int(input())
special_word = input()
phrases = []

for _ in range(cycles):
    phrases.append(input())

print(phrases)

print([phrase for phrase in phrases if special_word in phrase])
