# List - array -  ordered (indexed) collection of items - mutable, can have duplicates

# Set - unordered - not indexed - mutable

names_set = {'John', 'Jane', 'Stacy', 'Luke'}

# print(names_set)
# print(type(names_set))
# print(len(names_set)) # length

# print(names_set(1)) # will produce error - sets are unordered

names_set.add('Mary')
print(names_set)

names_set.remove('John')
print(names_set)

names_set.add('Jane') # has no effect because Jane already exists in the set
print(names_set)

set1 = {1, 2, 3, 4, 5}
set2 = { 1, 3, 5, 7, 9}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2 - set1)