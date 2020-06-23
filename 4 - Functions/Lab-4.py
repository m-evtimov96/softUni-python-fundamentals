def calculate_order(product, quantity):
    products = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }
    for ele, value in products.items():
        if product == ele:
            return quantity * value


product_in = input()
quantity_prod = int(input())

order = calculate_order(product_in, quantity_prod)
print(f'{order:.2f}')

