# A Python set is an unordered list of immutable elements. It means:

# Elements in a set are unordered.
# Elements in a set are unique. A set doesn’t allow duplicate elements.
# Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.
# To define a set in Python, you use the curly brace {}. For example:

skills = {'Python programming','Databases', 'Software design'}

# Note a dictionary also uses curly braces, but its elements are key-value pairs.

# To define an empty set, you cannot use the curly braces like this:

# empty_set = {}
# …because it defines an empty dictionary.

# Therefore, you need to use the built-in set() function:

empty_set  = set()

# An empty set evaluates to False in Boolean context. For example:

skills = set()

if not skills:
    print('Empty sets are falsy')


# In fact, you can pass an iterable to the set() function to create a set. 
# For example, you can pass a list, which is an iterable, to the set() function like this:

skills = set(['Problem solving','Critical Thinking'])
print(skills)

# Checking if an element is in a set
# To check if a set contains an element, you use the in operator:

# element in set

# The in operator returns True if the set contains the element. Otherwise, it returns False. For example:

ratings = {1, 2, 3, 4, 5}
rating = 1

if rating in ratings:
    print(f'The set contains {rating}')


# To add an element to a set, you use the add() method:

# set.add(element)

# Removing an element from a set
# To remove an element from a set, you use the remove() method:

# set.remove(element)

# To make it more convenient, the set has the discard() method that allows you to remove an element. 
# And it doesn’t raise an error if the element is not in the list:

# set.discard(element)

# Returning an element from a set
# To remove and return an element from a set, you use the pop() method.
# Since the elements in a set have no specific order, the pop() method removes an unspecified element from a set.
# If you execute the following code multiple times, it’ll show a different value each time:

skills = {'Problem solving', 'Software design', 'Python programming'}
skill = skills.pop()

print(skill)

# Frozen a set
# To make a set immutable, you use the built-in function called frozenset(). 
# The frozenset() returns a new immutable set from an existing one. For example:

skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)

# After that, if you attempt to modify elements of the set, you’ll get an error:

skills.add('Django')

# Looping through set elements
# Since a set is an iterable, you can use a for loop to iterate over its elements. For example:

skills = {'Problem solving', 'Software design', 'Python programming'}

for skill in skills:
    print(skill)

# To access the index of the current element inside the loop, you can use the built-in enumerate() function:

skills = {'Problem solving', 'Software design', 'Python programming'}

for index, skill in enumerate(skills):
    print(f"{index}.{skill}")


##### Python Set comprehension #####

# To make the code more concise, Python provides you with the set comprehension syntax as follows:

# {expression for element in set if condition}

# The set comprehension allows you to create a new set based on an existing set.
# A set comprehension carries the following steps:

# First, iterate over the elements of a set.
# Second, apply an expression to each element
# Third, create a new set of elements resulting from the expression.
# In addition, the set comprehension allows you to select which element to apply the expression via a condition in the if clause.
# Note that the set comprehension returns a new set, it doesn’t modify the original set.

tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)