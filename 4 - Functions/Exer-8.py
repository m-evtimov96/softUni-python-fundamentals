def visualize_loading(number):
    first_symbol = number // 10
    second_symbol = 10 - first_symbol
    loading_list = ['%'] * first_symbol
    loading_list.append('.' * second_symbol)
    print_string = ''.join(loading_list)
    if number == 100:
        print(f'{number}% Complete!')
        print(f'[{print_string}]')
    else:
        print(f'{number}% [{print_string}]')
        print('Still loading...')


number1 = int(input())
visualize_loading(number1)
