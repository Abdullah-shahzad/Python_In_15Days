"""
Author: Abdullah Shahzad
Created on: Sep 5, 2024
Surprise Task 4 by Sir Zaheer:

Task:
- Take input from the user (restricted integer).
- Create a function that works within a specific number range (2000 - 4700).
- Print numbers divisible by 7 but not divisible by 5, separated by commas.
"""

def integer_returner(num: int):
    """
    Checks if the number is divisible by 7 and not divisible by 5.

    @param num: Integer input to be checked.
    """
    if 2000 <= num <= 4700:
        if num % 5 != 0 and num % 7 == 0:
            list1.append(num)


list1 = []
n = 1

while n != 0:
    try:
        n = int(input("Enter an integer or enter 0 to exit: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if n != 0:
            integer_returner(n)

if list1:
    print("Numbers that satisfy the condition:", ", ".join(map(str, list1)))
else:
    print("No valid numbers were entered.")
