def greet(func):
    def wrapper():
        print("wrapper function")
        func()
        print("wrapper function 1")
    return wrapper

@greet
def hello():
    print("Hello there")


hello()

