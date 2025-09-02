letter = 'a'
value = ord(letter) - ord('a') + 1
print("Value:", value)

final_number = (value + 1 + 2 + 3 - 1) % 26 + 1
print("Final number:", final_number)

encrypted_letter = chr(final_number + ord('a') - 1)
print("Encrypted letter:", encrypted_letter)
