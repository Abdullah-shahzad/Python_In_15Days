def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b


x = y = 0
print("Select the operation you want to perform"
      "\n1: Addition"
      "\n2: Subtraction"
      "\n3: Division"
      "\n4: Multiplication"
      "\n5: Exit")

choice = int(input("Choice:"))
if choice in (1, 2, 3, 4):
    x = float(input("Enter the first number: "))
    y = float(input("Enter the first number: "))

if choice == 1:
    result = addition(x, y)
    print(f"{x} + {y} = {result}")
elif choice == 2:
    result = subtraction(x, y)
    print(f"{x} - {y} = {result}")
elif choice == 3:
    if y != 0:
        result = division(x, y)
        print(f"{x} / {y} = {result}")
    else:
        print("Error! Division by zero.")
elif choice == 4:
    result = multiplication(x, y)
    print(f"{x} * {y} = {result}")
elif choice == 5:
    print(f"______Thank you_______")
else:
    print("Please select the correct option")
