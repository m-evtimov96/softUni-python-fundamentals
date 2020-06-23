def repeat_by_len(s):
    return s * len(s)


words = input().split()
result = ''
for word in words:
    result += repeat_by_len(word)

print(result)
