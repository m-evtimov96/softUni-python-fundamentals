team_a = [item for item in range(1, 12)]
team_b = [item for item in range(1, 12)]
command_list = input().split(" ")

for command in command_list:
    if command[0] == 'A':
        if int(command[2:4]) in team_a:
            team_a.remove(int(command[2:4]))
    else:
        if int(command[2:4]) in team_b:
            team_b.remove(int(command[2:4]))

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if len(team_a) < 7 or len(team_b) < 7:
    print('Game was terminated')
