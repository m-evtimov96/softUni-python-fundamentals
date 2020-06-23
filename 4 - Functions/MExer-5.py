def find_result_type(num1, num2, num3):
    minuses = 0
    if num1 < 0:
        minuses += 1
    if num2 < 0:
        minuses += 1
    if num3 < 0:
        minuses += 1

    if num1 == 0 or num2 == 0 or num3 == 0:
        return 'zero'
    else:
        if minuses % 2 == 0:
            return 'positive'
        else:
            return 'negative'


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(find_result_type(num1, num2, num3))
