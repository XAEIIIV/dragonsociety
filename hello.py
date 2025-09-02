import itertools

# Define a list of numbers
my_list = input("Enter array").split()

# Generate all possible two-element combinations
# Convert the resulting iterator to a list
combinations = list(itertools.combinations(my_list, 8))

# Print the list of combinations to the console
print(combinations)

#Output: [(1, 2), (1, 3), (2, 3)]