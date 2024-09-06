import csv

# Data to be written to the CSV file
data = [
    ["Make", "Model", "Year", "Type", "Details"],
    ["Toyota", "Camry", "2022", "Car", "4 doors"],
    ["Ford", "F-150", "2021", "Truck", "1000 lbs cargo capacity"],
    ["Honda", "Civic", "2020", "Car", "4 doors"]
]

# Create and write to a CSV file
with open('vehicles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to vehicles.csv successfully.")


# Read from the CSV file
with open('vehicles.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
