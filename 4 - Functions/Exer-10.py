import sys


def exchange(array, index):
    if 0 <= index < len(array):
        first_half = array[0:index+1]
        second_half = array[index+1:len(array)+1]
        return second_half + first_half
    else:
        print(f'Invalid index')
        return array


def max_index(array, even_or_odd):
    max_indx = 0
    max_num = -sys.maxsize
    found_max = False
    if even_or_odd == 'even':
        for index, el in enumerate(array):
            if el % 2 == 0 and el >= max_num:
                max_num = el
                max_indx = index
                found_max = True
    elif even_or_odd == 'odd':
        for index, el in enumerate(array):
            if el % 2 != 0 and el >= max_num:
                max_num = el
                max_indx = index
                found_max = True
    if found_max:
        print(max_indx)
    else:
        print('No matches')


def min_index(array, even_or_odd):
    min_indx = 0
    min_number = sys.maxsize
    found_min = False
    if even_or_odd == 'even':
        for index, el in enumerate(array):
            if el % 2 == 0 and el <= min_number:
                min_number = el
                min_indx = index
                found_min = True
    elif even_or_odd == 'odd':
        for index, el in enumerate(array):
            if el % 2 != 0 and el <= min_number:
                min_number = el
                min_indx = index
                found_min = True
    if found_min:
        print(min_indx)
    else:
        print('No matches')


def return_first(array, counter, even_or_odd):
    return_list = []
    counter = int(counter)
    if counter <= len(array):
        for el in array:
            if even_or_odd == 'even' and el % 2 == 0 and counter > 0:
                return_list.append(el)
                counter -= 1
            elif even_or_odd == 'odd' and el % 2 != 0 and counter > 0:
                return_list.append(el)
                counter -= 1
        print(return_list)
    else:
        print('Invalid count')


def return_last(array, counter, even_or_odd):
    return_list = []
    counter = int(counter)
    if counter <= len(array):
        for el in reversed(array):
            if even_or_odd == 'even' and el % 2 == 0 and counter > 0:
                return_list.append(el)
                counter -= 1
            elif even_or_odd == 'odd' and el % 2 != 0 and counter > 0:
                return_list.append(el)
                counter -= 1
        print(return_list[::-1])
    else:
        print('Invalid count')


work_array = [int(x) for x in input().split(' ')]

while True:
    command = input().split(' ')
    if command[0] == 'end':
        break
    elif command[0] == 'exchange':
        work_array = exchange(work_array, int(command[1]))
    elif command[0] == 'max':
        max_index(work_array, command[1])
    elif command[0] == 'min':
        min_index(work_array, command[1])
    elif command[0] == 'first':
        return_first(work_array, command[1], command[2])
    elif command[0] == 'last':
        return_last(work_array, command[1], command[2])


print(work_array)
