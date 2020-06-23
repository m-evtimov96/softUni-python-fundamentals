neighborhood = list(map(int, input().split('@')))
house_index = 0

while True:
    command = input().split()
    if command[0] == 'Love!':
        break

    jump_len = int(command[1])
    if house_index + jump_len >= len(neighborhood):
        house_index = 0
    else:
        house_index += jump_len

    if neighborhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        neighborhood[house_index] -= 2
        if neighborhood[house_index] <= 0:
            print(f"Place {house_index} has Valentine's day.")

neighborhood = [house for house in neighborhood if house != 0]
print(f"Cupid's last position was {house_index}.")
if neighborhood:
    print(f"Cupid has failed {len(neighborhood)} places.")
else:
    print("Mission was successful.")
