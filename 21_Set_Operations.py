# set union
# The union of two sets returns a new set that contains distinct elements from both sets.

# s1 = {'Python', 'Java'}
# s2 = {'C#', 'Java'}
# The union of the s1 and s2 sets return the following set:
# {'Java','Python', 'C#'}

# In Python, to union two or more sets, you use the union() method:

# new_set = set.union(another_set, ...)

# The following example shows how to union the s1 and s2 sets:

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
s = s1.union(s2)
print(s)


# Union sets using the | operator
# Python provides you with the set union operator | that allows you to union two sets:

# new_set = set1 | set2
# The set union operator (|) returns a new set that consists of distinct elements from both set1 and set2.

# The following example shows how to use the union operator (|) to union the s1 and s2 sets:

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}
s = s1 | s2
print(s)

# the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.
# The following example shows how to pass a list to the union() method:

rates = {1, 2, 3}
ranks = [2, 3, 4]
ratings = rates.union(ranks)
print(ratings)


# However, the union operator (|) only allows sets, not iterables like the union() method.
# The following example causes an error:

# rates = {1, 2, 3}
# ranks = [2, 3, 4]
# ratings = rates | ranks



# In Python, you can use the set intersection() method or set intersection operator (&) to intersect two or more sets:

# new_set = set1.intersection(set2, set3)
# new_set = set1 & set2 & set3

# When intersecting two or more sets, you’ll get a new set consisting of elements that exist in all sets.
# Suppose that you have two following sets s1 and s2:

# s1 = {'Python', 'Java','C++'}
# s2 = {'C#', 'Java', 'C++' }

# The intersection of these two sets returns a new set that contains two elements 'Java' and 'C++':

# s = {'Java', 'C++'}
# because they’re the only elements that exist in both sets.

# new_set = set1.intersection(set2, set3, ...)

# new_set = s1 & s2 & s3 & ...

# The set intersection operator only allows sets, while the set intersection() method can accept any iterables, 
# like strings, lists, and dictionaries.

# If you pass iterables to the intersection() method, it’ll convert the iterables to set before intersecting them.

# However, the set intersection operator (&) will raise an error if you use it with iterables.

##### Python Set difference #####
# The difference between the two sets results in a new set that has elements from the first set which aren’t present in the second set.

# Suppose you have the following s1 and s2 sets:

# s1 = {'Python', 'Java', 'C++'}
# s2 = {'C#', 'Java', 'C++'}

# The difference between s1 and s2 sets results in the following set with one element:

# {'Python'}

# because there is only 'Python' element from the first set that doesn’t exist in the second set.
# The set difference isn’t commutative. The difference between the s2 and s1 sets returns the following set:

# {'C#'}

# The Set type has a difference() method that returns the difference between two or more sets:

# set1.difference(s2, s3, ...)

# Besides the difference() method, Python provides you with 
# the set difference operator (-) that allows you to find the difference between sets.

# s = s1 - s2

# The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) 
# while the set difference operator (-) only allows sets.

# When you pass iterables to the set difference() method, it’ll convert the iterables to sets before performing the difference operation.


# The symmetric difference between two sets is a set of elements that are in either set, but not in their intersection.
# Suppose that you have the following s1 and s2 sets:

# s1 = {'Python', 'Java', 'C++'}
# s2 = {'C#', 'Java', 'C++'}

# The symmetric difference of the s1 and s2 sets returns in the following set:

# {'C#', 'Python'}

# As you can see clearly from the output, the elements in the return set are either in s1 or s2 set, but not in their intersection.

# The Set type has the symmetric_difference() method that returns the symmetric difference of two or more sets:

# new_set = set1.symmetric_difference(set2, set3,...)

# Besides using the set symmetric_difference() method, you can use 
# the symmetric difference operator (^) to find the symmetric difference between two or more sets:

# new_set = set1 ^ set2 ^...

# The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.
# If the iterables aren’t sets, the method will convert them to sets before returning the symmetric difference of them.



##### Python issubset() method #####
# Suppose that you have two sets A and B. 
# Set A is a subset of set B if all elements of A are also elements of B. Then, set B is a superset of set A.

# Set A and set B can be equal. If set A and set B are not equal, A is a proper subset of B.
# In Python, you can use the Set issubset() method to check if a set is a subset of another:

# set_a.issubset(set_b)
# If the set_a is a subset of the set_b, the issubset() method returns True. Otherwise, it returns False.

# Besides using the issubset() method, you can use the subset operator (<=) to check if a set is a subset of another set:

# set_a <= set_b
# The subset operator (<=) returns True if set_a is a subset of the set_b. Otherwise, it returns False

# The proper subset operator (<) check if the set_a is a proper subset of the set_b:

# set_a < set_b


##### Python issuperset method #####
# Suppose that you have two sets: A and B. Set A is a superset of set B if all elements of set B are elements of set A.
# If set A is a superset of set B, then set B is a subset of set A. To check if a set is a subset of another, you use the issubset() method.
# If set A and set B are not equal, set A is a proper superset of set B.
# Logically, a set is a superset of itself.

# In Python, you use the set issuperset() method to check if a set is a superset of another set:

# set_a.issuperset(set_b)

# The issuperset() returns True if the set_a is a superset of the set_b. Otherwise, it returns False.

# Using superset operators
# The >= operator determines if a set is a superset of another set:

# set_a >= set_b

# The >= operator returns True if the set_a is a superset of the set_b. Otherwise, it returns False


##### Python disjoint sets #####
# Two sets are disjoint when they have no elements in common. 
# In other words, two disjoint sets are sets whose intersection is an empty set.

# For example, the {1,3,5} and {2,4,6} sets are disjoint because they have no common elements.

# In Python, you use the Set isdisjoint() method to check if two sets are disjoint or not:

# set_a.isdisjoint(set_b)

# The isdisjoint() method returns True if the set_a and set_b are disjoint. Otherwise, it returns False.
# The isdisjoint() method also accepts any iterable, not just a set.
# If you pass a list, a tuple, or a dictionary, the isdisjoint() method will convert it to a set before checking.