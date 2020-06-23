prices_dict = {}
quantity_dict = {}

while True:
    input_line = input().split()
    if input_line[0] == 'buy':
        break
    name = input_line[0]
    price = float(input_line[1])
    quantity = int(input_line[2])

    prices_dict.setdefault(name, 0)
    prices_dict[name] = price
    quantity_dict.setdefault(name, 0)
    quantity_dict[name] += quantity

for product in prices_dict.keys():
    total = prices_dict[product] * quantity_dict[product]
    print(f"{product} -> {total:.2f}")
