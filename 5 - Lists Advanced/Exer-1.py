def filter_list(func_list):
    for el in list2:
        if func_list in el:
            return True
    return False


list1 = input().split(', ')
list2 = input().split(', ')

result_list = list(filter(filter_list, list1))
print(result_list)