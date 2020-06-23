num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2:
    if num1 > num3:
        biggest = num1
    else:
        biggest = num3
elif num2 > num3:
    biggest = num2
else:
    biggest = num3

print(biggest)