def repeat_string(string_rep, cycle):
    return string_rep * cycle


string_to_rep = input()
repeats = int(input())

repeated_string = repeat_string(string_to_rep, repeats)
print(repeated_string)
