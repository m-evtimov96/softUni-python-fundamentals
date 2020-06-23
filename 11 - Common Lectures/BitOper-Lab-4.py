number = int(input())
position = int(input())

binary_num_rev = (bin(number)[2:])[::-1]
new_number = binary_num_rev[:position] + "0" + binary_num_rev[position+1:]
new_num_rev = new_number[::-1]

print(int(new_num_rev, 2))
