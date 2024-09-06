"""
Surprise Task 3 by Sir Zaheer
you have to take string from user
* Handle all the exceptional cases
* Check if its a palindrome or not
* Also remove the vowel from the user given string and then print it
"""

def palindrome(mystring):
    print("Given :", mystring)
    reverse_str = mystring[::-1]
    print("Reversed :", reverse_str)
    if mystring == reverse_str:
        print("its a palindrome")

    else:
        print("its not a palindrome")


userinput1 = input("please enter a string or str if its palindrome or not :")
if userinput1 != "" and " " not in userinput1:
    palindrome(userinput1)
    if 'a' in userinput1:
        userinput1 = userinput1.replace("a", "")
        print(userinput1)
    if 'o' in userinput1:
        userinput1 = userinput1.replace("o", "")
        print(userinput1)
    if 'i' in userinput1:
        userinput1 = userinput1.replace("i", "")
        print(userinput1)
    if 'u' in userinput1:
        userinput1 = userinput1.replace("u", "")
        print(userinput1)
    if 'e' in userinput1:
        userinput1 = userinput1.replace("e", "")
        print(userinput1)

else:
    print("please enter a proper string with out space")
