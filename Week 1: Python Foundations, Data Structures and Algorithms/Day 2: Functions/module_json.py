import json

#basically there is only 4 things in json load,loads, dumps ,dump
#dump for writting in the file
#load for getting data from json file
#dumps for converting the python dict or list into json string
#loads for converting the json string into the python dict

# Python dictionary
data = {
    "name": "John Wick",
    "age": 30,
    "is_employee": True,
    "skills": ["Python", "Django", "Machine Learning"]
}
print("As a dict: ",data)

# Convert Python dictionary to JSON string
json_string = json.dumps(data, indent=2)
print("\nJSON string:", json_string)

####################################################################################

# JSON string
json_string = '{"name": "John Doe", "age": 30, "is_employee": true, "skills": ["Python", "Django", "Machine Learning"]}'
print(json_string)
# Convert JSON string to Python dictionary
data = json.loads(json_string)
print("Python dictionary:", data)
print("Name:", data['name'])

#######################################################################

# Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "is_employee": True,
    "skills": ["Python", "Django", "Machine Learning"]
}

# Write the dictionary to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been written to data.json")

#######################################################################

# Read the JSON file and parse it into a Python dictionary
with open('data.json', 'r') as file:
    data = json.load(file)

print("Data read from file:", data)
print("Skills:", data['skills'])

