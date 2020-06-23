items = input().split('|')

while True:
    command = input().split(' ')
    if command[0] == 'Yohoho!':
        break
    elif command[0] == 'Loot':
        for item in command[1::]:
            if item not in items:
                items.insert(0, item)
    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(items):
            items.append(items.pop(index))
    elif command[0] == 'Steal':
        counts_stolen = int(command[1])
        stolen_items = []

        if counts_stolen > len(items):
            counts_stolen = len(items)

        stolen_items = items[-counts_stolen::]
        for _ in range(counts_stolen):
            items.pop()

        print(', '.join(stolen_items))

if items:
    average_sum = 0
    for item in items:
        average_sum += len(item)
    average_sum = average_sum/len(items)
    print(f'Average treasure gain: {average_sum:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
