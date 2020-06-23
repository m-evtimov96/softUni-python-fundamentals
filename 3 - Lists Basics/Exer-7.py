gifts = input().split(' ')

while True:
    command = input().split(' ')
    if (' '.join(command)) == 'No Money':
        break
    else:
        if command[0] == 'OutOfStock':
            gifts[:] = [None if x == command[1] else x for x in gifts]
        elif command[0] == 'Required':
            if 0 <= int(command[2]) < len(gifts):
                gifts[int(command[2])] = command[1]
        elif command[0] == 'JustInCase':
            gifts[len(gifts)-1] = command[1]

gifts = [i for i in gifts if i]
print(' '.join(gifts))
