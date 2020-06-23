stock = {}

while True:
    command = input()
    if command == 'statistics':
        break
    else:
        product, quantity = command.split(': ')

    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

print('Products in stock:')
for product, quantity in stock.items():
    print(f'- {product}: {quantity}')
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")
