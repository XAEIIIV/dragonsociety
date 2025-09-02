rotor1 = 1
rotor2 = 2
rotor3 = 3

def machine():
    initial = input("Type letter (a–z): ").lower()

    if initial.isalpha() and len(initial) == 1:
        value = ord(initial) - ord('a') + 1
        total = value + rotor1 + rotor2 + rotor3
        final_number = (total - 1) % 26 + 1
        encrypted_letter = chr(final_number + ord('a') - 1)

        print("Encrypted number:", final_number)
        print("Encrypted letter:", encrypted_letter)
    else:
        print("Invalid input.")

machine()
