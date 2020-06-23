encrypted_message = list(input())
number_list = [char for char in encrypted_message if char.isdigit()]
non_nums_list = [char for char in encrypted_message if not char.isdigit()]
print(number_list)
print(non_nums_list)
take_list = []
skip_list = []
for index, num in enumerate(number_list):
    if index == 0 or index % 2 == 0:
        take_list.append(num)
    else:
        skip_list.append(num)
print(take_list)
print(skip_list)

# Finish this