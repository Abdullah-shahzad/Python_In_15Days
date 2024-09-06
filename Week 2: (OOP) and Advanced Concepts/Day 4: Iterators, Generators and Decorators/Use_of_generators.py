def fibonacci():
    """A generator to yield an infinite sequence of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(10):  # Generate the first 10 Fibonacci numbers
    print(next(fib))

##########################################################################