# function overloading
def add(*nums):
   return sum(nums)


# Call the function with different number of parameters
result1 = add(10, 25)
result2 = add(10, 25, 35)

print(result1)
print(result2)

###############################################################

# operator overloading
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        # overloading
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
# overloading
print(v1 + v2)