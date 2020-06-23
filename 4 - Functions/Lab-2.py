def calculate(operator, num1, num2):
    if operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return num1 / num2


operator_in = input()
first_number = int(input())
second_number = int(input())

result = calculate(operator_in, first_number, second_number)
print(int(result))
