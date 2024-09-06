for x in range(4):
    print(x)
#############################

for x in range(2,9,2):
    print(x)

###############################

count = 0
while count < 5:
    print(count)
    count += 1

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

#####################################################

for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")
    