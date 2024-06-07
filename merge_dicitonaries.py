def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Test the function
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(merge_dicts(dict1, dict2))  
