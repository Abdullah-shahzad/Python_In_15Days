class EvenNumbers:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        return self.current

class Squares:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = self.current ** 2
            self.current += 1
            return result


# Using the Squares iterator
squares = Squares(1, 5)
evens = EvenNumbers()

# Combining iterators
for square, even in zip(squares, evens):
    print(f"Square: {square}, Even: {even}")
