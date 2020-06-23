def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


commands_num = int(input())
parking_lot = {}

for _ in range(commands_num):
    input_line = input().split()
    command = input_line[0]
    if command == 'register':
        name = input_line[1]
        l_plate = input_line[2]
        if name in parking_lot:
            print(f'ERROR: already registered with plate number {parking_lot[name]}')
        else:
            parking_lot[name] = l_plate
            print(f'{name} registered {l_plate} successfully')

    elif command == 'unregister':
        name = input_line[1]
        if name not in parking_lot:
            print(f'ERROR: user {name} not found')
        else:
            parking_lot.pop(name)
            print(f'{name} unregistered successfully')

print_dict(parking_lot, "{} => {}")
