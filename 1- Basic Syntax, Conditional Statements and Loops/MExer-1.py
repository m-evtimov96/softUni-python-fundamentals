number = input()

digit_list = [int(x) for x in number]
digit_list.sort(reverse=True)
bigest_num = ''.join(map(str, digit_list))
print(bigest_num)
