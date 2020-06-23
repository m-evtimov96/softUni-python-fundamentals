from itertools import zip_longest
string1, string2 = input().split(' ')
total = 0

for s1, s2 in zip_longest(string1, string2):
    if s1 and s2:
        total += ord(s1) * ord(s2)
    elif s1:
        total += ord(s1)
    elif s2:
        total += ord(s2)

print(total)
