companies = {}

while True:
    input_line = input()
    if input_line == 'End':
        break
    input_line = input_line.split(' -> ')
    company = input_line[0]
    employee_id = input_line[1]

    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

companies = dict(sorted(companies.items()))
for company, employees in companies.items():
    employees = "\n-- ".join(employees)
    print(company)
    print(f'-- {employees}')
