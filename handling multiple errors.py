try:
    with open("non_existent_file.txt", 'r') as file:
        contents = file.read()
        num = int(contents)
        print("Integer value:", num)
except FileNotFoundError:
    print("Error: File not found")
except ValueError:
    print("Error: Contents cannot be converted to integer")
except IOError:
    print("Error: Unable to read file")
