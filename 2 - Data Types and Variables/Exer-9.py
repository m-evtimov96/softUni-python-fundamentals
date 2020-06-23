snowballs_nums = int(input())
best_value = 0

for i in range(snowballs_nums):
    sb_snow = int(input())
    sb_time = int(input())
    sb_quality = int(input())
    sb_value = int(sb_snow / sb_time) ** sb_quality
    if sb_value > best_value:
        best_value = sb_value
        best_snow = sb_snow
        best_time = sb_time
        best_quality = sb_quality

print(f'{best_snow} : {best_time} = {best_value} ({best_quality})')
