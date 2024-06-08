def print_square():
    try:
        num = int(input("Enter an integer: "))
        square = num ** 2
        print("Square of", num, "is", square)
    except ValueError:
        print("Error: Please enter a valid integer!")

# Example usage:
print_square()
