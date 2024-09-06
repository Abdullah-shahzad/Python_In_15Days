def fab(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
        print(a)


user_input = int(input("Enter any number :"))
fab(user_input)
