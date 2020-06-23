wagons = int(input())
train = [0] * wagons

while True:
    command = input()
    tokens = command.split(' ')
    instruction = tokens[0]

    if instruction == 'End':
        break

    elif instruction == 'add':
        count_people = int(tokens[1])
        train[-1] += count_people
    elif instruction == 'insert':
        index = int(tokens[1])
        count_people = int(tokens[2])
        train[index] += count_people
    elif instruction == 'leave':
        index = int(tokens[1])
        count_people = int(tokens[2])
        train[index] -= count_people

print(train)
