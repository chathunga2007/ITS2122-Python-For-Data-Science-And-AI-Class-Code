class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute initialized
        self.__balance = 0
        self.set_balance(initial_balance)

    # Setter method with validation
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid balance")

    # Getter method
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")


# Testing all methods
if __name__ == "__main__":
    # Create an object
    account = BankAccount(1000)
    print(f"Current Balance: {account.get_balance()}")

    # Test setter validation
    account.set_balance(-200)   # Output: Invalid balance
    account.set_balance(1500)
    print(f"Updated Balance: {account.get_balance()}")

    # Test deposit
    account.deposit(500)
    print(f"Balance after deposit: {account.get_balance()}")

    # Test withdraw (sufficient balance)
    account.withdraw(800)
    print(f"Balance after withdrawal: {account.get_balance()}")

    # Test withdraw (insufficient balance)
    account.withdraw(2000)     # Output: Insufficient balance
    print(f"Final Balance: {account.get_balance()}")