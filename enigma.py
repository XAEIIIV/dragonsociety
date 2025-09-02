# Enigma-style simulator with persistent rotors, plugboard, and looping encrypt/decrypt
rotor1 = 1
rotor2 = 1
rotor3 = 1
plugboard = {}

def rotors():
    global rotor1, rotor2, rotor3
    r1 = input("Set rotor 1 (1–26): ")
    if r1 == "exit": return
    r2 = input("Set rotor 2 (1–26): ")
    if r2 == "exit": return
    r3 = input("Set rotor 3 (1–26): ")
    if r3 == "exit": return
    rotor1 = int(r1)
    rotor2 = int(r2)
    rotor3 = int(r3)
    print(f"Rotors set to {rotor1}, {rotor2}, {rotor3}")
    start()

def add1():
    global rotor1, rotor2, rotor3
    rotor1 += 1
    if rotor1 > 26:
        rotor1 = 1
        rotor2 += 1
        if rotor2 > 26:
            rotor2 = 1
            rotor3 += 1
            if rotor3 > 26:
                rotor3 = 1

def plug():
    global plugboard
    plugboard = {}
    print("Enter plugboard pairs (e.g. ab swaps a↔b). Type 'done' to finish or 'exit' to quit.")
    while True:
        pair = input("Pair: ").lower()
        if pair == "exit":
            return
        if pair == "done":
            break
        if len(pair) == 2 and pair[0].isalpha() and pair[1].isalpha():
            a, b = pair[0], pair[1]
            plugboard[a] = b
            plugboard[b] = a
        else:
            print("Invalid pair. Try again.")
    print("Plugboard configured:", plugboard)
    start()

def swap(letter):
    return plugboard.get(letter, letter)

def process(letter, mode):
    global rotor1, rotor2, rotor3
    if not letter.isalpha():
        return letter

    letter = swap(letter)
    value = ord(letter) - ord('a') + 1

    if mode == "encrypt":
        total = value + rotor1 + rotor2 + rotor3
    else:  # decrypt
        total = value - rotor1 - rotor2 - rotor3

    final_number = (total - 1) % 26 + 1
    result = chr(final_number + ord('a') - 1)
    result = swap(result)
    add1()
    return result

def machine(mode):
    global rotor1, rotor2, rotor3
    while True:
        message = input(f"Enter message to {mode} (or 'exit' to return): ").lower()
        if message == "exit": break

        # Save rotor state
        r1, r2, r3 = rotor1, rotor2, rotor3

        result = []
        for letter in message:
            result.append(process(letter, mode))

        print(f"{mode.title()}ed message:", ''.join(result))

        # Restore rotor state
        rotor1, rotor2, rotor3 = r1, r2, r3
    start()

def start():
    print("\n--- Enigma Simulator ---")
    print("1: Set Rotors")
    print("2: Configure Plugboard")
    print("3: Encrypt Message")
    print("4: Decrypt Message")
    print("5: Exit")
    choice = input("Choose: ")
    if choice == "exit" or choice == "5":
        print("Goodbye!")
    elif choice == "1":
        rotors()
    elif choice == "2":
        plug()
    elif choice == "3":
        machine("encrypt")
    elif choice == "4":
        machine("decrypt")
    else:
        print("Invalid choice.")
        start()

start()