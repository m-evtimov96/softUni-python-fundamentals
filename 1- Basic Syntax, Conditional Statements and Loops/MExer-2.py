input_string = input()
index_list = []

for char in range(len(input_string)):
    if 65 <= ord(input_string[char]) <= 90:
        index_list.append(char)

print(index_list)
