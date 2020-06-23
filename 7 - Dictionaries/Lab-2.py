def get_stock(raw_data):
    data = raw_data.split(' ')
    return {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}


def check_availability(product):
    if product in food_list:
        print(f'We have {food_list[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")


food_list = get_stock(input())
check_list = input().split(' ')

[check_availability(product) for product in check_list]
