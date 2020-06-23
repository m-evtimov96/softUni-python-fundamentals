rooms_num = int(input())
rooms = []
free_chairs = 0
for room in range(rooms_num):
    rooms.append(input().split(' '))

for index, room in enumerate(rooms):
    chairs = len(room[0])
    taken = int(room[1])
    free = chairs - taken
    if free > 0:
        free_chairs += free
    elif free < 0:
        print(f'{abs(free)} more chairs needed in room {index+1}')
        free_chairs += free

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')

