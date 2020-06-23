def char_between(start_char, end_char):
    range_string = ''
    for ascii_code in range(ord(start_char)+1, ord(end_char)):
        range_string += f'{chr(ascii_code)} '

    return range_string


char1 = input()
char2 = input()
print(char_between(char1, char2))
