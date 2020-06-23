from math import ceil

num_list = list(map(int, input().split(', ')))
max_num = max(num_list)
groups_count = ceil(max_num / 10)

for group in range(1, groups_count + 1):
    max_bord = group * 10
    min_bord = max_bord - 10
    current_group = [num for num in num_list if min_bord < num <= max_bord]
    print(f"Group of {group*10}'s: {current_group}")