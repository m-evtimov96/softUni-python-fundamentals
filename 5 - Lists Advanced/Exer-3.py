current_version = list(reversed(input().split('.')))
for index, el in enumerate(current_version):
    if el == '9':
        current_version[index] = '0'
    if el != '9':
        current_version[index] = str(int(el) + 1)
        break
print('.'.join(reversed(current_version)))
