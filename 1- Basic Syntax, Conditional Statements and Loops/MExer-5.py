coffee = 0
commands_list = ['coding', 'dog', 'cat', 'movie']
commands_list_upper = ['CODING', 'DOG', 'CAT', 'MOVIE']

while True:
    command = input()

    if command == 'END':
        break
    if command in commands_list:
        coffee += 1
    elif command in commands_list_upper:
        coffee += 2

if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)
