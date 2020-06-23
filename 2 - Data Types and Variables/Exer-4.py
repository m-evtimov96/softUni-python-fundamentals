num_chars = int(input())
char_sum = 0

for i in range(num_chars):
    char = input()
    char_sum += ord(char)

print(f'The sum equals: {char_sum}')