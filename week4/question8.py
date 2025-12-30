class ATM:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited successfully"
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"{amount} withdrawn successfully"
    def get_balance(self):
        return self.balance
