resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break

    amount = int(input())
    resources.setdefault(resource, 0)
    resources[resource] += amount

    # if resource in resources:
    #     resources[resource] += amount
    # else:
    #     resources[resource] = amount

for resource, amount in resources.items():
    print(f'{resource} -> {amount}')
