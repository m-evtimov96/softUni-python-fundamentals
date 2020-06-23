cycles = int(input())
positive_nums = []
negative_nums = []

for i in range(cycles):
    number = int(input())
    if number < 0:
        negative_nums.append(number)
    else:
        positive_nums.append(number)

print(positive_nums)
print(negative_nums)
print(f'Count of positives: {len(positive_nums)}. Sum of negatives: {sum(negative_nums)}')
