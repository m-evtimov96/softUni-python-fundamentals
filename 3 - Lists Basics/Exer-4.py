numbers_list = input().split(", ")
num_beggars = int(input())
beggars_list = [0] * num_beggars
counter = 0

for element in numbers_list:
    beggars_list[counter] += int(element)
    if counter >= num_beggars-1:
        counter = 0
    else:
        counter += 1

print(beggars_list)


