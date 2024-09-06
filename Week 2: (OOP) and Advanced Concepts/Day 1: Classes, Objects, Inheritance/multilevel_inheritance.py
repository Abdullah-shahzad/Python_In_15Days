# parent class
class Universe:
    def universeMethod(self):
        print("I am in the Universe")


# child class
class Earth(Universe):
    def earthMethod(self):
        print("I am on Earth")


# grandchild class
class Pakistan(Earth):
    def pakistaniMethod(self):
        print("I am in Pakistan")

    # creating instance


person = Pakistan()
# method calls
person.universeMethod()
person.earthMethod()
person.pakistaniMethod()