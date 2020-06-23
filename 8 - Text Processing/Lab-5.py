# def get_numbers(s):
#     result = ''
#     for char in s:
#         if char.isdigit():
#             result += char
#     return result
#
#
# def get_letters(s):
#     result = ''.join(filter(str.isalpha, s))
#     return result
#
#
# def get_others(s):
#     pass
#
#
# input_string = input()
# print(get_numbers(input_string))
# print(get_letters(input_string))
# print(get_others(input_string))

text = input()
digits = ''
letters = ''
other = ''

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other += char

print(f'{digits}\n{letters}\n{other}')
