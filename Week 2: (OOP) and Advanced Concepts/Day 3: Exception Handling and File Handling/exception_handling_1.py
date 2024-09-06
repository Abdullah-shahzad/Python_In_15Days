try:
    nominator = float(input("Enter a number (nominator): "))
    de_nominator = float(input("Enter a number (de-nominator): "))
    result = nominator/de_nominator

except ValueError as e:
    print(e)
    print("Error: please enter a correct value(number)")

except ZeroDivisionError as e:
    print(e)
    print("Error: can't divide by zero")
else:
    print(f"{nominator} / {de_nominator} = {result}")


###############################################################################
class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class InputTooSmallError(CustomError):
    """Raised when the input value is too small."""
    def __init__(self, message="Input is too small"):
        self.message = message
        super().__init__(self.message)

class InputTooLargeError(CustomError):
    """Raised when the input value is too large."""
    def __init__(self, message="Input is too large"):
        self.message = message
        super().__init__(self.message)

def check_input(value):
    if value < 10:
        raise InputTooSmallError(f"Input value {value} is too small.")
    elif value > 100:
        raise InputTooLargeError(f"Input value {value} is too large.")
    return f"Input value {value} is within the acceptable range."

try:
    check_input(5)
except CustomError as e:
    print(f"Custom error caught: {e}")
