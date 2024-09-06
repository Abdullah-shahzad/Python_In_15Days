numbers = [12, 13, 14,]
doubled = [x / 2 for x in numbers]
print(doubled)
##########################################

numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)

########################################

list = [i for i in range(11) if i % 2 == 0]
print(list)

###########################################

matrix = [[j for j in range(1)] for i in range(4)]
print(matrix)

#################################################

List = [character for character in 'Geeks 4 Geeks!']
print(List)

###################################################
names = ["G", "G", "g"]
ages = [25, 30, 35]
person_tuples = [(name, age) for name, age in zip(names, ages)]
print(person_tuples)
##################################################
words = ["apple", "banana", "cherry", "orange"]
word_lengths = [len(word) for word in words]
print(word_lengths)


