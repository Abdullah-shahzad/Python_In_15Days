def count_frequency_of_char(mystring1):
    frequency = {}
    for char in mystring1:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


mystring = "abdullah_shahzad"
mydict = count_frequency_of_char(mystring)

print(mydict)
for i in mydict.items():
    print(i)
