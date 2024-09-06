
name = "Abdullah"
print("Hello, %s!" % name)


name = "John"
age = 23
print("%s is %d years old." % (name, age))


mylist = [1,2,3]
print("A list: %s" % mylist)


data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string, "%s %s. Your current balance is  $%d" % data)

######################################################################## python.org solution
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)


#########################################################

astring = "Hello world!"
print(astring.index("w"))

###############################################################

astring = "Hello world!"
print(astring.count("l"))
######################################################
astring = "12345"
print(astring[::-1])
 ###########################################
astring = "Hello world!"
print(astring[::-1])

#########################################
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

##########################################

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

########################################################
a_string = "Hello world!"
a_string_split = a_string.split(" ")
print(a_string_split)