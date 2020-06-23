path_string = input()
file_string = ''

for char in reversed(path_string):
    if char == "\\":
        file = ''.join(reversed(file_string)).split('.')
        break
    file_string += char

print(f'File name: {file[0]}')
print(f'File extension: {file[1]}')
