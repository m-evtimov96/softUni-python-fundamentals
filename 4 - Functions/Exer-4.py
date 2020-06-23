def calc_even_odd(number):
    even_sum = 0
    odd_sum = 0
    for digit in map(int, number):
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


number1 = input()
print(calc_even_odd(number1))
