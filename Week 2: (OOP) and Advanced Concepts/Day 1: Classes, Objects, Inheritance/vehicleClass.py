class Vehicle:

    def __init__(self, vehicle_type, colour, make, model, year, num_wheels, num_doors, fuel_type):
        self.vehicle_type = vehicle_type
        self.colour = colour
        self.make = make
        self.model = model
        self.year = year
        self.num_wheels = num_wheels
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def printout(self):
        if self.vehicle_type == "car":
            print("its a car")
        elif self.vehicle_type == "car":
            print("its a truck")
        print("This", self.vehicle_type, "has", self.colour, "colour ")
        print("Its", self.make, self.model, self.year)
        print("It has", self.num_wheels, "wheels and", self.num_doors, "doors",)
        print("fuel type", self.fuel_type)


obj1 = Vehicle("car", "silver","Honda", "Reborn",2011,4,4,"Gasoline")

for i in range(5):
    obj1.printout()
    print("_________________________________")
