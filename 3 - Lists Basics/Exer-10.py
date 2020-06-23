energy = 100
coins = 100
events_list = input().split('|')
bankrupt = False

for events in events_list:
    event = events.split('-')
    task = event[0]
    price = int(event[1])

    if task == 'rest':
        if energy == 100:
            energy_gained = 0
        elif energy + price >= 100:
            energy_gained = 100 - price
            energy = 100
        else:
            energy_gained = price
            energy += price
        print(f'You gained {energy_gained} energy.')
        print(f'Current energy: {energy}.')
    elif task == 'order':
        if energy - 30 >= 0:
            coins += price
            energy -= 30
            print(f'You earned {price} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - price > 0:
            coins -= price
            print(f'You bought {task}.')
        else:
            print(f'Closed! Cannot afford {task}.')
            bankrupt = True
            break

if not bankrupt:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
