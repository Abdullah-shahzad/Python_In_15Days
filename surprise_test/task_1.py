"""
Surprise Task 2 by Sir Zaheer
you have to create a list of 100 random integers
* Find the count of even number in it
* Find the average of even number in it
* Find the second largest in the whole list
"""

import random
list1 = []
for j in range(100):
    list1.append(random.randint(0, 1000))

print(len(list1))

list2 = []
addition = 0

for i in list1:
    if i % 2 == 0:
        list2.append(i)
        addition += i

length = len(list2)
print("Count of even number", length)
average = addition/length
print("Average of even number:", average)
sortedlist = list1.sort()
print("Second Largest number is :", list1[-2])



