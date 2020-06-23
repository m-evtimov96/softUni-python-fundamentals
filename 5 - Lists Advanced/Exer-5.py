electrons = int(input())
electron_list = []
n = 1
while electrons > 0:
    shell = 2*n**2
    if electrons >= shell:
        electron_list.append(shell)
        electrons -= shell
    else:
        electron_list.append(electrons)
        electrons = 0
    n += 1

print(electron_list)