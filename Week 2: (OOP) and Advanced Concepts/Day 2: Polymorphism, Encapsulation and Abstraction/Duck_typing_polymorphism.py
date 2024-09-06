class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

# Polymorphic behavior
dog = Dog()
cat = Cat()
print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!

