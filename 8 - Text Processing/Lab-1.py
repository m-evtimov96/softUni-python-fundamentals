def reverse_string(s):
    return "".join(reversed(s))


result = {}

while True:
    input_string = input()
    if input_string == 'end':
        break
    result[input_string] = reverse_string(input_string)

for k, v in result.items():
    print(f"{k} = {v}")
