numbers_list = list(map(int, input().split(' ')))
number = int(input())

for _ in range(number):
    numbers_list.remove(min(numbers_list))

print(numbers_list)
