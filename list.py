from functools import reduce

# List manipulation methods
my_list = []

# append() method
my_list.append(1)
my_list.append(2)
my_list.append(3)

# insert() method
my_list.insert(1, 1.5)

# remove() method
my_list.remove(2)

# reverse() method
my_list.reverse()

# clear() method
my_list.clear()

# List comprehension
my_list = [x for x in range(10) if x % 2 == 0]


# Indexing and slicing
print(my_list[0])      # Output: 0
print(my_list[1:4])    # Output: [2, 4, 6]


# Special methods: map, filter, reduce, zip
# map() method
doubled_list = list(map(lambda x: x * 2, my_list))
print(doubled_list)    # Output: [0, 4, 8, 12, 16]

# filter() method
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print(even_numbers)    # Output: [0, 2, 4, 6, 8]

# reduce() method
total_sum = reduce(lambda x, y: x + y, my_list)
print(total_sum)       # Output: 20

# zip() method
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
zipped_list = list(zip(letters, numbers))
print(zipped_list)     # Output: [('a', 1), ('b', 2), ('c', 3)]
