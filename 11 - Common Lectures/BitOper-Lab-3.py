number = int(input())
position = int(input())

shifted_binary_number = bin(number >> position)[2:]
print(shifted_binary_number[::-1][0:1])
