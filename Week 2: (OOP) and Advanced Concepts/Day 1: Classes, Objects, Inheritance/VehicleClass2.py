class Vehicle:
    def __init__(self):
        self.vehicle_type = None
        self.colour = None
        self.make = None
        self.model = None
        self.year = None
        self.num_wheels = None
        self.num_doors = None
        self.fuel_type = None

    def input(self):
        print("Enter the type of vehicle (e.g., car, truck, jeep, etc.):")
        self.vehicle_type = input()

        print("Enter the colour of the vehicle:")
        self.colour = input()

        print("Enter the make of the vehicle (e.g., Toyota, Ford):")
        self.make = input()

        print("Enter the model of the vehicle (e.g., Corolla, raptor):")
        self.model = input()

        print("Enter the year of the vehicle:")
        self.year = input()

        print("Enter the number of wheels:")
        self.num_wheels = input()

        print("Enter the number of doors:")
        self.num_doors = input()

        print("Enter the fuel type (e.g., Gasoline, Diesel, Electric):")
        self.fuel_type = input()

    def printout(self):
        if self.vehicle_type == "car":
            print("It's a car")
        elif self.vehicle_type == "truck":
            print("It's a truck")
        elif self.vehicle_type == "jeep":
            print("It's a jeep")
        else:
            print(f"It's a {self.vehicle_type}")

        print("This", self.vehicle_type, "has", self.colour, "colour.")
        print("It's a", self.make, self.model, self.year)
        print("It has", self.num_wheels, "wheels and", self.num_doors, "doors.")
        print("Fuel type:", self.fuel_type)


vehicle = Vehicle()
vehicle.input()
vehicle.printout()
