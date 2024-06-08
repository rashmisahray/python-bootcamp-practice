try:
    print(undefined_variable)
except NameError:
    print("Error: Variable is not defined")

try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")

