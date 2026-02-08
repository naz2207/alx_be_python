# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to control the number of rows
while row < size:
    # For loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    
    # Increment the row counter
    row += 1
