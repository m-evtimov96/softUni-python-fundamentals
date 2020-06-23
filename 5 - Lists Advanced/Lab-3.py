def is_palindrome(word):
    return word == word[::-1]


strings_list = input().split(' ')
key_palindrome = input()

palindrome_list = [word for word in strings_list if is_palindrome(word)]
palindromes_found = palindrome_list.count(key_palindrome)

print(palindrome_list)
print(f'Found palindrome {palindromes_found} times')