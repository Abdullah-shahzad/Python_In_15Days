"""
Surprise Task 2 by Sir Zaheer
you have to create a list of 100 random integers
* Find the count of even number in it
* Find the average of even number in it
* Find the second largest in the whole list
* In whole program you can use only one loop
"""

import random

list1 = []
list2 = []
loop_counter = 100
addition = 0
largest = 0
second_largest = 0

while loop_counter:
    number = random.randint(0, 1000)
    list1.append(number)

    if number % 2 == 0:
        list2.append(number)
        addition += number

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

    loop_counter -= 1

length = len(list2)
print("Count of even numbers:", length)

average = addition / length
print("Average of even numbers:", average)

print("Second largest number is:", second_largest)
