number = int(input())
binary_digit = input()

binary_number = bin(number)[2:]
counter = 0

for digit in binary_number:
    if digit == binary_digit:
        counter += 1

print(counter)
