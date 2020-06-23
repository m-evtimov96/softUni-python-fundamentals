input_string = "".join(input().split())
char_dict = {}

for char in input_string:
    char_dict.setdefault(char, 0)
    char_dict[char] += 1

    # if char in char_dict.keys():
    #     char_dict[char] += 1
    # else:
    #     char_dict[char] = 1

for char, value in char_dict.items():
    print(f"{char} -> {value}")
