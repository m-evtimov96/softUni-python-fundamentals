numbers_list = [int(i) for i in input().split(', ')]
list_with_zero = []

for index, num in enumerate(numbers_list):
    if num == 0:
        list_with_zero.append(numbers_list[index])

numbers_list[:] = (value for value in numbers_list if value != 0)
numbers_list.extend(list_with_zero)
print(numbers_list)
