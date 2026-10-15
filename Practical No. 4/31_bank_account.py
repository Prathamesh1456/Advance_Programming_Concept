class BankAccount:

    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful.")
        else:
            print("Insufficient balance for transfer.")


account1 = BankAccount("Atharva")
account2 = BankAccount("Rahul")

account1.deposit(10000)
account1.withdraw(2000)

account1.transfer(3000, account2)

print("\nAccount 1:")
account1.display_balance()

print("\nAccount 2:")
account2.display_balance()