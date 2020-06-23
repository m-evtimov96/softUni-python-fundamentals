def tribonacci(num):
    trib_list = []
    if num == 1:
        trib_list = [1]
    elif num == 2:
        trib_list = [1, 1]
    elif num >= 3:
        trib_list = [1, 1, 2]

    for i in range(3, num):
        trib_list.append(trib_list[i-1]+trib_list[i-2]+trib_list[i-3])

    print(' '.join(str(x) for x in trib_list))


num_in = int(input())
tribonacci(num_in)
