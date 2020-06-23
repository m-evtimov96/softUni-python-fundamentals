num1 = int(input())
num2 = int(input())
num3 = int(input())
biggest = 0

if num1 > num2 and num1 > num3:
    biggest = num1
elif num2 > num1 and num2 > num3:
    biggest = num2
else:
    biggest = num3

print(biggest)
