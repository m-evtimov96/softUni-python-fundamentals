def sum_numbers(number1, number2):
    result = number1 + number2
    return result


def subtract(number1, number2):
    sub_result = number1 - number2
    return sub_result


def add_and_subtract(number1, number2, number3):
    sum_result = sum_numbers(number1, number2)
    end_result = subtract(sum_result, number3)
    return end_result


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))
