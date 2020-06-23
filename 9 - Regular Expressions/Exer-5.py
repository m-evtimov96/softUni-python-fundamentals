import re

pattern = r"^>>(?P<item>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<count>\d+)$"

bought_products = []
total = 0
while True:
    line = input()
    if line == "Purchase":
        break

    products = re.finditer(pattern, line)
    for product in products:
        bought_products.append(product.group("item"))
        total += float(product.group("price")) * int(product.group("count"))

print("Bought furniture:")
for item in bought_products:
    print(item)
print(f"Total money spend: {total:.2f}")
