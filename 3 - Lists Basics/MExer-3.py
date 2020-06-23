starting_list = input().split(' ')
count_value = int(input())
counter = count_value
new_list = []

while len(starting_list) != 0:
    # print(len(starting_list))
    for index in range(count_value - 1, len(starting_list), count_value):
        print(starting_list[index])
        new_list.append(starting_list.pop(count_value))

    print(starting_list)
    print(new_list)

# Finish this