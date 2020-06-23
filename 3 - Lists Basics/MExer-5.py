initial_energy = 100
initial_coins = 100
work_day_events = input().split('|')
energy = initial_energy
coins = initial_coins
is_closed = False
for i in range(len(work_day_events)):
    current_command = work_day_events[i].split('-')
    event = current_command[0]
    quantity = int(current_command[1])

    if event == 'rest':
        if energy + quantity <= initial_energy:
            print(f'You gained {quantity} energy.')
            energy += quantity
        else:
            print(f'You gained {initial_energy - energy} energy.')
            energy = initial_energy

        print(f'Current energy: {energy}.')

    elif event == 'order':
        energy -= 30
        if energy >= 0:
            print(f'You earned {quantity} coins.')
            coins += quantity
        else:
            print(f'You had to rest!')
            energy += 80

    else:
        if coins < quantity:
            print(f'Closed! Cannot afford {event}.')
            is_closed = True
            break
        else:
            print(f'You bought {event}.')
            coins -= quantity

if not is_closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')