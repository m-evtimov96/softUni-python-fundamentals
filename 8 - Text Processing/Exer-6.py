from itertools import groupby
text = input()
trimmed_text = ''.join(char[0] for char in groupby(text))
print(trimmed_text)
