first_string = input()
second_string = input()
print_string = first_string

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        for str_second in range(0, i+1):
            print(second_string[str_second], end="")
        for str_first in range(i+1, len(first_string)):
            print(first_string[str_first], end="")

        print()
