key = int(input())
cycles = int(input())
decrypted_massage = ''

for i in range(cycles):
    char = input()
    decrypted_massage += chr(ord(char) + key)

print(decrypted_massage)
