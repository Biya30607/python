class BankAccount:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient Balance")

account = BankAccount(101, "Alice", "Savings", 5000)
account.deposit(1000)
account.withdraw(2000)
account.withdraw(5000)

