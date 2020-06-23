input_list = input().split('#')
water = int(input())
total_fire = 0
effort = 0

print('Cells:')
for cell in input_list:
    fire = cell.split(' ')
    fire_level = int(fire[2])
    # print(fire)
    if fire[0] == 'High' and 81 <= fire_level <= 125:
        if fire_level <= water:
            water -= fire_level
            print(f' - {fire_level}')
            total_fire += fire_level
            effort += 0.25 * fire_level
    elif fire[0] == 'Medium' and 51 <= fire_level <= 80:
        if fire_level <= water:
            water -= fire_level
            print(f' - {fire_level}')
            total_fire += fire_level
            effort += 0.25 * fire_level
    elif fire[0] == 'Low' and 1 <= fire_level <= 50:
        if fire_level <= water:
            water -= fire_level
            print(f' - {fire_level}')
            total_fire += fire_level
            effort += 0.25 * fire_level

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
