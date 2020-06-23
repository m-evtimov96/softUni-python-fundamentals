animals = []

while True:
    command = input()
    if command == 'Last Info':
        break
    else:
        command_list = command.split(':')
        if command_list[0] == 'Add':
            command_list.remove('Add')
            animal_check = [el for el in animals if el[0] == command_list[0]]
            if animal_check:
                # print(animals)
                animals.remove(animal_check[0])
                feed_to_add = int(animal_check[0][1]) + int(command_list[1])
                feed_to_add = str(feed_to_add)
                animal_check[0][1] = feed_to_add
                animals.append(animal_check[0])
                # print(animals)
            else:
                animals.append(command_list)

        elif task == 'Feed':
            pass
        # write code for Feed