import time

def calculating_the_time(func):
    def wrapper_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        time_taken = (end - start)
        print(f"The total time taken by: {func.__name__} is {time_taken:.5f} seconds")

    return wrapper_func

@calculating_the_time
def fibonacci_func(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = b, a + b


@calculating_the_time
def addition_func(a, b):

    print(a + b)


fibonacci_func(5)
addition_func(20, 50)
