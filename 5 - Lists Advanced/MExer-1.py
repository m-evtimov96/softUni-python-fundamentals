def sum_digits(number):
    result = 0
    while number:
        result, number = result + number % 10, number // 10
    return result


def make_message(indexes, string):
    string_list = list(string)
    message = ''
    for index in indexes:
        if index >= len(string_list):
            index -= len(string_list)
        message += string_list[index]
        del string_list[index]
    return message


num_list = list(map(int, input().split(' ')))
string_in = input()
index_list = list(map(sum_digits, num_list))
print(make_message(index_list, string_in))
