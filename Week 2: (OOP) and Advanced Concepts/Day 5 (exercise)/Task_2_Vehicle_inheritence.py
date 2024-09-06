"""
Author: Abdullah Shahzad
created on: July 31, 2023,
modified on: Aug 01, 2023,
modified on: Aug 28, 2024
"""

class Vehicle:
    """
    A class representing a general vehicle.
    """

    def __init__(self, make, model, year):
        """
        Initialise a vehicle.
        @param make: The make of the vehicle.
        @param model: The model of the vehicle.
        @param year: The manufacturing year of the vehicle.
        """
        self.make = make
        self.model = model
        self.year = year


    def info(self):
        """
        Provide the vehicle's information.
        :return Basic information of vehicle. (string)
        """

        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    """
    A class representing a car, inheriting from Vehicle.
    """

    def __init__(self, make, model, year, num_doors):
        """
        Constructor for Car class.
        @param make: The make of the car.
        @param model: The model of the car.
        @param year: The manufacturing year of the car.
        @param num_doors: The number of doors in the car.
        """

        super().__init__(make, model, year)
        self.num_doors = num_doors

    def info(self):
        """
        @return: the car's information with the number of doors.
        """

        return f"{super().info()} with {self.num_doors} doors."


class ElectricCar(Car):

    """
    A class representing an electric car, inheriting from Car.
    """

    def __init__(self, make, model, year, num_doors, battery_capacity):
        """
        Constructor for ElectricCar class.
        @param make: The make of the electric car. (string)
        @param model: The model of the electric car. (string)
        @param year: The manufacturing year of the electric car. (int)
        @param num_doors: The number of doors in the electric car. (int)
        @param battery_capacity: The battery capacity of the electric car in kWh.
        """

        super().__init__(make, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def info(self):
        """
        @return: the electric car's information with battery capacity.
        """

        return f"{super().info()} It's an electric car with battery capacity: {self.battery_capacity} kWh."


class Motorcycle(Vehicle):
    """
    A class representing a motorcycle, inheriting from Vehicle.
    """

    def __init__(self, make, model, year, num_wheels):
        """
        Constructor for Motorcycle class.
        @param make: The make of the motorcycle.
        @param model: The model of the motorcycle.
        @param year: The manufacturing year of the motorcycle.
        @param num_wheels: The number of wheels in the motorcycle.
        """
        super().__init__(make, model, year)

        self.num_wheels = num_wheels

    def info(self):
        """
        @return : the motorcycle's information with the number of wheels.
        """

        return f"{super().info()} with {self.num_wheels} wheels."


car1 = Car("Toyota", "Camry", 2022, 4)
electric_car1 = ElectricCar("Tesla", "Model S", 2023, 4, 100)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2021, 2)

print(car1.info())
print(electric_car1.info())
print(motorcycle1.info())
