def are_happy(employee_list):
    avg_happiness = sum(employee_list) / len(employee_list)
    happy_list = [el for el in employee_list if el >= avg_happiness]
    len_employee = len(employee_list)
    len_happy = len(happy_list)
    if len_happy >= len_employee / 2:
        print(f'Score: {len_happy}/{len_employee}. Employees are happy!')
    else:
        print(f'Score: {len_happy}/{len_employee}. Employees are not happy!')


happiness_list = list(map(int, input().split()))
improv_factor = int(input())

happiness_list = [el * improv_factor for el in happiness_list]
are_happy(happiness_list)
