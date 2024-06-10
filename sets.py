from itertools import combinations, product

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union, Difference, Intersection, Symmetric Difference
union_set = set1.union(set2)
difference_set = set1.difference(set2)
intersection_set = set1.intersection(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

# Powerset of a set using combinations() from itertools
def powerset(s):
    return [set(combo) for i in range(len(s)+1) for combo in combinations(s, i)]

powerset_set1 = powerset(set1)

# Cartesian product of two sets using product() from itertools
cartesian_product = list(product(set1, set2))

# Frozen Set - Immutable version of set
frozen_set = frozenset(set1)

# Set Algebra
# Check for subset and superset
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)

# Output results
print("Union:", union_set)
print("Difference:", difference_set)
print("Intersection:", intersection_set)
print("Symmetric Difference:", symmetric_difference_set)
print("Powerset of set1:", powerset_set1)
print("Cartesian Product of set1 and set2:", cartesian_product)
print("Frozen Set:", frozen_set)
print("Is set1 a subset of set2:", is_subset)
print("Is set1 a superset of set2:", is_superset)
