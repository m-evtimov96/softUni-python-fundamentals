num1 = int(input())
num2 = int(input())

print('Before:')
print(f'a = {num1}')
print(f'b = {num2}')

temp = num2
num2 = num1
num1 = temp

print('After:')
print(f'a = {num1}')
print(f'b = {num2}')
