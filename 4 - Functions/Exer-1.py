def find_smallest(number1, number2, number3):
    num_list = [number1, number2, number3]
    num_list.sort()
    return num_list[0]


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(find_smallest(num1, num2, num3))
