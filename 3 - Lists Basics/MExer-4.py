rows = int(input())
battleground = []
sunk_ships = 0
for i in range(rows):
    row = list(map(int, input().split(' ')))
    battleground.append(row)

commands = input().split(' ')

for attacks in commands:
    attack = attacks.split('-')
    row = int(attack[0])
    column = int(attack[1])

    if battleground[row][column] != 0:
        battleground[row][column] -= 1
        if battleground[row][column] == 0:
            sunk_ships += 1

print(sunk_ships)
