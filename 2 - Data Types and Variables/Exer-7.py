tank_capacity = 255
cycles = int(input())

for i in range(cycles):
    liters_to_pour = int(input())
    if liters_to_pour <= tank_capacity:
        tank_capacity -= liters_to_pour
    else:
        print('Insufficient capacity!')

print(255 - tank_capacity)
