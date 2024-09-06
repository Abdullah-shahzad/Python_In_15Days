try:
    n = int(input("enter any number"))
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

except ValueError as e:
    print(e)

