def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero!"
    else:
        return result

# Test the function
print(divide(10, 2))   
print(divide(10, 0))   
