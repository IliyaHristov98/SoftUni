key = int(input())
lines = int(input())
decrypted_message = ''
for n in range(lines):
    letter = input()
    decrypted_letter = chr(ord(letter) + key)
    decrypted_message += decrypted_letter
print(decrypted_message)
