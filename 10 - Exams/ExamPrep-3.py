pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
game_over = False

def is_valid(index, limit):
    return 0 <= index < limit

while True:
    line = input().split()
    command = line[0]

    if command == 'Retire':
        break
    elif command == 'Fire':
        index = int(line[1])
        damage = int(line[2])
        if is_valid(index, len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                game_over = True
                break
    elif command == 'Defend':
        start_index = int(line[1])
        end_index = int(line[2])
        damage = int(line[3])
        both_are_valid = all([is_valid(start_index, len(pirate_ship)), is_valid(end_index, len(pirate_ship))])
        if both_are_valid:
            for zone in range(start_index, end_index+1):
                pirate_ship[zone] -= damage
                if pirate_ship[zone] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    game_over = True
                    break
    elif command == 'Repair':
        index = int(line[1])
        health = int(line[2])
        if is_valid(index, len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    elif command == 'Status':
        counter = 0
        for zone in pirate_ship:
            if zone < max_health * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')

if not game_over:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')
