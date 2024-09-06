class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder  # Protected variable
        self.__balance = initial_balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self._validate_withdrawal(amount):  # Using protected method
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.__balance

    def _validate_withdrawal(self, amount):  # Protected method
        return amount <= self.__balance

    def __apply_interest(self, rate):  # Private method
        interest = self.__balance * rate
        self.__balance += interest
        print(f"Applied interest of ${interest}. New balance: ${self.__balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)




# Example usage
account = SavingsAccount("John Doe", 1000)
account.deposit(500)  # Deposit $500
account.withdraw(2000)  # Withdraw $200
print(f"Current balance: ${account.get_balance()}")  # Check balance

