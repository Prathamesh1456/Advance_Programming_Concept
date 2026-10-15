#24.	Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.
def deposit(balance, amount, transaction_history):
    balance += amount
    transaction_history.append(f"Deposited: {amount}")
    return balance
def withdraw(balance, amount, transaction_history):
    if amount > balance:
        print("Insufficient balance for withdrawal.")
        return balance
    balance -= amount
    transaction_history.append(f"Withdrew: {amount}")
    return balance
def balance_enquiry(balance):
    print(f"Current Balance: {balance}")
def transaction_history(transaction_history):
    print("Transaction History:")
    for transaction in transaction_history:
        print(transaction)
def main():
    balance = 0
    transaction_history_list = []
    while True:
        print("\nBanking System Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount, transaction_history_list)
            print(f"Deposited: {amount}. New Balance: {balance}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount, transaction_history_list)
            print(f"New Balance: {balance}")
        elif choice == '3':
            balance_enquiry(balance)
        elif choice == '4':
            transaction_history(transaction_history_list)
        elif choice == '5':
            print("Exiting the banking system.")
            break
        else:
            print("Invalid choice. Please try again.")