import math

#for float
number = 7.4
print(number.__floor__())
print(number.__ceil__())

#for non-negative number and also it always return a float
n = -7.4
a = -10
print(n,a)
print(math.fabs(n), math.fabs(a))

# same purpose as fabs but there is no need to import math
x = abs(-7.25)

print(x)

#factorial
z = 5
print(math.factorial(z))

#sum
l = [123.1, 123.2, 123.4, 123.3]
print(math.fsum(l))

#min max
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#pi
x = math.pi
print(x)

#sqr root
num = 16
n = math.sqrt(num)
print(n)