numbers = list(map(int, input().split(', ')))

print([index for index, el in enumerate(numbers) if el % 2 == 0])

