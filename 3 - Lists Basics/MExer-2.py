matrix = []
for i in range(3):
    row = list(map(int, input().split(' ')))
    matrix.append(row)

if (all(p == 1 for p in matrix[0]) or all(p == 1 for p in matrix[1]) or all(p == 1 for p in matrix[2])) or \
    (matrix[0][0] == matrix[1][0] == matrix[2][0] == 1 or matrix[0][1] == matrix[1][1] == matrix[2][1] == 1 or
        matrix[0][2] == matrix[1][2] == matrix[2][2] == 1) or \
        (matrix[0][0] == matrix[1][1] == matrix[2][2] == 1 or matrix[0][2] == matrix[1][1] == matrix[2][0] == 1):
    print('First player won')
elif (all(p == 2 for p in matrix[0]) or all(p == 2 for p in matrix[1]) or all(p == 2 for p in matrix[2])) or \
    (matrix[0][0] == matrix[1][0] == matrix[2][0] == 2 or matrix[0][1] == matrix[1][1] == matrix[2][1] == 2 or
        matrix[0][2] == matrix[1][2] == matrix[2][2] == 2) or \
        (matrix[0][0] == matrix[1][1] == matrix[2][2] == 2 or matrix[0][2] == matrix[1][1] == matrix[2][0] == 2):
    print('Second player won')
else:
    print('Draw!')

# Refactor This!