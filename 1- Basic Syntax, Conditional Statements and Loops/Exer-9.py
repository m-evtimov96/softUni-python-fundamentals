budget = float(input())
flour_price = float(input())
egg_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4
kozunak_price = flour_price + egg_price + milk_price
kozunaks = 0
coloured_eggs = 0

while True:
    if budget > kozunak_price:
        budget -= kozunak_price
        kozunaks += 1
        if kozunaks % 3 == 0:
            coloured_eggs += 3
            coloured_eggs -= kozunaks - 2
        else:
            coloured_eggs += 3
    else:
        break

print(f'You made {kozunaks} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')
