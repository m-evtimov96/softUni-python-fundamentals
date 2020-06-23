def binary_to_decimal(num):
    binary_num = num[::-1]
    decimal_num = 0
    for position in range(0, len(binary_num)):
        decimal_num += int(binary_num[position]) * (2 ** position)
    return decimal_num


def decimal_to_binary(decimal_num):
    binary_num = ''
    while decimal_num > 0:
        binary_num += str(decimal_num % 2)
        decimal_num = decimal_num // 2
    return binary_num[::-1]


print(decimal_to_binary(8623232))
print(binary_to_decimal('10101011011100'))
