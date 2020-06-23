number = int(input())

for numb in range(1, number+1):

    digit_sum = sum(map(int, str(numb)))
    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
    print(f'{numb} -> {is_special}')


