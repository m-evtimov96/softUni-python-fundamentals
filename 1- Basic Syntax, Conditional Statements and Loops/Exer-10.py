quantity = int(input())
days = int(input())
cost = 0
spirit = 0

for day in range(1, days +1 ):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        cost += 2 * quantity
        spirit += 5
    if day % 3 == 0:
        cost += 8 * quantity
        spirit += 13
    if day % 5 == 0:
        cost += 15 * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        cost += 23
        spirit -= 20
if days % 10 == 0:
    spirit -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')
