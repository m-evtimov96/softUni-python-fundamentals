import math


def factorial_division(number1, number2):
    fac_number1 = math.factorial(number1)
    fac_number2 = math.factorial(number2)
    result = fac_number1 / fac_number2
    return result


num1 = int(input())
num2 = int(input())
print(f'{factorial_division(num1, num2):.2f}')
