employee1_eff = int(input())
employee2_eff = int(input())
employee3_eff = int(input())
total_people = int(input())
answers_per_hour = employee1_eff + employee2_eff + employee3_eff
hour = 1

while total_people > 0:
    if hour % 4 != 0:
        total_people -= answers_per_hour
    hour += 1

print(f'Time needed: {hour - 1}h.')
