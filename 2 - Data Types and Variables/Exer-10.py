losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_shield = 0

for lost in range(1, losses+1):
    if lost % 2 == 0:
        expenses += helmet_price
    if lost % 3 == 0:
        expenses += sword_price
        if lost % 2 == 0:
            expenses += shield_price
            broken_shield += 1
            if broken_shield == 2:
                expenses += armor_price
                broken_shield = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')
