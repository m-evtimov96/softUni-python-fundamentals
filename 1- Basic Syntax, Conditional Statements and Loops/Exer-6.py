int_year = int(input()) + 1
year = str(int_year)

while True:
    symbols = len(year)
    unique_symbols = len(set(year))

    if symbols == unique_symbols:
        print(year)
        break
    else:
        int_year += 1
        year = str(int_year)



# in_year = input()
# distinct = False
#
# while not distinct:
#     in_year = str(in_year)
#     if in_year[1] != in_year[0] and in_year[1] != in_year[2] and in_year[1] != in_year[3] \
#             and in_year[2] != in_year[0] and in_year[2] != in_year[3] and in_year[3] != in_year[0]:
#         print(in_year)
#         distinct = True
#     else:
#         in_year = int(in_year)
#         in_year += 1

# Rework this code !
