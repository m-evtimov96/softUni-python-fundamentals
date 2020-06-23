cycles = int(input())
balanced = True
opened = False
counter = 0

for i in range(cycles):
    char = input()
    if char == ')'and counter == 0:
        balanced = False
    if opened:
        if char == ')':
            opened = False
            counter -= 1
        elif char == '(':
            balanced = False
    if char == '(':
        opened = True
        counter += 1
if counter == 0 and balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
