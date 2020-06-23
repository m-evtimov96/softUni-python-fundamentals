deck = input().split(" ")
shuffles = int(input())

for _ in range(shuffles):
    first_half = deck[0:int(len(deck)/2)]
    second_half = deck[int(len(deck)/2):int(len(deck)+1)]
    deck.clear()
    for num1, num2 in zip(first_half, second_half):
        deck.append(num1)
        deck.append(num2)

print(deck)
