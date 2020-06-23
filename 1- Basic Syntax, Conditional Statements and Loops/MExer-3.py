animals = input()
animal_list = animals.split(", ")

if animal_list[len(animal_list) - 1] == "wolf":
    print('Please go away and stop eating my sheep')
else:
    counter = 0
    for animal_number in range(len(animal_list) - 1, -1, -1):
        if animal_list[animal_number] == "wolf":
            print(f'Oi! Sheep number {counter}! You are about to be eaten by a wolf!')
        counter += 1
