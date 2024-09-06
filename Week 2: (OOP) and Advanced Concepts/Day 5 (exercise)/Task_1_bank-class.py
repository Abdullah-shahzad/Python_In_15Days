class Bank:
    def __init__(self, balance =10000):
        self.balance = balance

    def deposit_func(self, deposit):
        print(f"Balance Before Deposit = {self.balance}")
        self.balance += deposit
        print(f"Balance After Deposit = {self.balance}")


    def withdraw_func(self, withdraw):
        if withdraw <= self.balance:
            print(f"Balance Before Withdrawal = {self.balance}")
            self.balance -= withdraw
            print(f"Balance After Withdrawal = {self.balance}")
        else:
            print("Insufficient balance")

    def balance_checker(self):
        print(f"Your current balance is :{self.balance}")



if __name__ == '__main__':
    bank = Bank()
    while True:
        print("\n--------------------------\n"
              "1: Deposit\n"
              "2: Withdraw\n"
              "3: Balance check\n"
              "4: Exit")
        choice = int(input("Enter you choice: "))
        match choice:
            case 1:
                dep = float(input("Enter amount to deposit:"))
                bank.deposit_func(dep)

            case 2:
                withdraw_am = float(input("Enter amount for withdrawal:"))
                bank.withdraw_func(withdraw_am)
            case 3:
                bank.balance_checker()
            case 4:
                break
            case _:
                print("Please enter a valid choice")




