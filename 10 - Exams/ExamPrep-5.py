friends_list = input().split(', ')
blacklisted_count = 0
lost_count = 0

while True:
    line = input().split(' ')
    command = line[0]
    if command == 'Report':
        print(f'Blacklisted names: {blacklisted_count}')
        print(f'Lost names: {lost_count}')
        print(' '.join(friends_list))
        break
    elif command == 'Blacklist':
        name = line[1]
        if name in friends_list:
            friends_list[:] = ['Blacklisted' if el == name else el for el in friends_list]
            print(f'{name} was blacklisted.')
            blacklisted_count += 1
        else:
            print(f'{name} was not found.')
    elif command == 'Error':
        index = int(line[1])
        if friends_list[index] != 'Blacklisted' and friends_list[index] != 'Lost':
            print(f'{friends_list[index]} was lost due to an error.')
            friends_list[index] = 'Lost'
            lost_count += 1
    elif command == 'Change':
        index = int(line[1])
        new_name = line[2]
        if 0 <= index < len(friends_list):
            print(f'{friends_list[index]} changed his username to {new_name}.')
            friends_list[index] = new_name
