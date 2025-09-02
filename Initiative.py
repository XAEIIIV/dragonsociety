def order_initiatives():
    initiatives = []
    
    while True:
        initiative = input("Enter player initiative (or press Enter to finish): ")
        if initiative == "":
            break
        try:
            initiatives.append(int(initiative))
        except ValueError:
            print("Please enter a valid number.")
    
    sorted_initiatives = sorted(initiatives, reverse=True)
    
    print("\nInitiatives in descending order:")
    for i, initiative in enumerate(sorted_initiatives, 1):
        print(f"{i}. Initiative: {initiative}")

order_initiatives()