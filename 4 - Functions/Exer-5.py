def check_if_palindrom(numbers_list):
    for number in numbers_list:
        if str(number) == str(number)[::-1]:
            print('True')
        else:
            print('False')


num_list = input().split(', ')
check_if_palindrom(num_list)
