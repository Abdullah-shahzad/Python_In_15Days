"""
MAP function
Filter
Reduce
lamda
Zip
"""

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

# Using map to add corresponding elements
summed = map(lambda x, y: x + y, numbers1, numbers2)

print(list(summed))

#####################################################

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = zip(list1, list2)
print("using zip function to combine to lists",list(merged))

##########################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))

#######################################################

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce to multiply elements
product = reduce(lambda x, y: x * y, numbers)

print(product)

########################################################

fruits = ['apple', 'banana', 'cherry']

# Using enumerate to get index and value
for index, value in enumerate(fruits):
    print(index, value)
