# Tuple creation
my_tuple = (1, 2, 3, 4, 5)

#len() function
print(len(my_tuple))  # Output: 5

# min() and max() functions
print(min(my_tuple))  # Output: 1
print(max(my_tuple))  # Output: 5

# sorted() function
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # Output: [1, 2, 3, 4, 5]

# count() method
print(my_tuple.count(3))  # Output: 1

# asterisk (*) function
first, *middle, last = my_tuple
print(first, middle, last)  # Output: 1 [2, 3, 4] 5

# Indexing and slicing
print(my_tuple[0])     # Output: 1
print(my_tuple[1:4])   # Output: (2, 3, 4)

# More functions
# len() 
length = len(my_tuple)
print(length)  # Output: 5

# min() 
minimum = min(my_tuple)
print(minimum)  # Output: 1

# max() 
maximum = max(my_tuple)
print(maximum)  # Output: 5

# sorted() 
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # Output: [1, 2, 3, 4, 5]

# count() 
count_three = my_tuple.count(3)
print(count_three)  # Output: 1
