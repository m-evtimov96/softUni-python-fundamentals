food_list = input().split()

bakery = {}
for i in range(0, len(food_list), 2):
    key = food_list[i]
    value = food_list[i + 1]
    bakery[key] = int(value)

print(bakery)