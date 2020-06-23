num_stars = int(input())

for i in range(1, num_stars+1):
    print('*' * i)
for i in range(num_stars-1, 0, -1):
    print('*' * i)


# for i in range(1, num_stars+1):
#     for j in range(0, i):
#         print('*', end='')
#     print('')
# for i in range(num_stars-1, 0, -1):
#     for j in range(0, i):
#         print('*', end='')
#     print('')