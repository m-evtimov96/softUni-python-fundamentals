def calculate_time(track):
    finish_line = len(track) // 2
    car_time = 0
    for step in range(finish_line):
        if track[step] == 0:
            car_time *= 0.8
        else:
            car_time += track[step]
    return f'{car_time:.1f}'


track_list = [int(num) for num in input().split()]
left_car_time = calculate_time(track_list)
track_list.reverse()
right_car_time = calculate_time(track_list)

if left_car_time > right_car_time:
    winner = 'left'
    winner_time = left_car_time
else:
    winner = 'right'
    winner_time = right_car_time
print(f'The winner is {winner} with total time: {winner_time}')

# fix this
