input_list = input().split('|')
budget = float(input())
starting_money = budget
profit = 0

for ele in input_list:
    purchase = ele.split('->')
    item = purchase[0]
    price = float(purchase[1])
    if item == 'Clothes' and price <= 50 and budget - price >= 0:
        budget -= price
        sell_price = price*1.4
        profit += sell_price
        print(f'{sell_price:.2f}', end=' ')
    elif item == 'Shoes' and price <= 35 and budget - price >= 0:
        budget -= price
        sell_price = price*1.4
        profit += sell_price
        print(f'{sell_price:.2f}', end=' ')
    elif item == 'Accessories' and price <= 20.50 and budget - price >= 0:
        budget -= price
        sell_price = price*1.4
        profit += sell_price
        print(f'{sell_price:.2f}', end=' ')

money_made = budget + profit


print(f'\nProfit: {profit+budget-starting_money:.2f}')

if money_made >= 150:
    print('Hello, France!')
else:
    print('Time to go.')