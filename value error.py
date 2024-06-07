def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            break  # Break out of the loop if input is successfully converted to an integer
        except ValueError:
            print("Error: Please enter a valid integer!")
    return value

# Test the function
age = get_integer_input("Enter your age: ")
print("Age entered:", age)
