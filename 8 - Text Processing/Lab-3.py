keyword = input()
s = input()

while True:
    if keyword not in s:
        break
    s = s.replace(keyword, "")

print(s)
