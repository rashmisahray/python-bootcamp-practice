def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])

# Test the function
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 18}
]
print(sort_dicts_by_key(students, "age")) 
