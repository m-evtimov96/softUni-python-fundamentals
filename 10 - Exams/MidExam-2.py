shopping_list = input().split('!')

while True:
    line = input()

    if line == 'Go Shopping!':
        break
    else:
        line = line.split()
        command = line[0]

    if command == 'Urgent':
        item = line[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif command == 'Unnecessary':
        item = line[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif command == 'Correct':
        old_name = line[1]
        new_name = line[2]
        shopping_list = [new_name if el == old_name else el for el in shopping_list]
    elif command == 'Rearrange':
        item = line[1]
        if item in shopping_list:
            shopping_list.append(shopping_list.pop(shopping_list.index(item)))

print(', '.join(shopping_list))
