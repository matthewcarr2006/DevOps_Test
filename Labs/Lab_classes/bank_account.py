# 2. Create a BankAccount class with attributes account_number and balance. 
# Add methods to deposit and withdraw money from the account. 

class BankAccount:
    def __init__(self, account_number, sort_code, business, balance=0):
        self.account_number = account_number
        self.sort_code = sort_code
        self.business = business
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Depost: £{amount} >>> New balance: £{self.balance}"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawl: £{amount} >>> New balance: £{self.balance}"
        elif amount > self.balance:
            return "You have insufficient funds to make this withdrawal."
        else:
            return "Please anter a value greater than zero in order to make a withdrawal."

    def get_balance(self):
        return f"Account balance: £{self.balance}"



my_account = BankAccount("12345678","12-34-56", False)
print(f"Account: {my_account.account_number}, Sort: {my_account.sort_code}")

print(my_account.deposit(500))
print(my_account.withdraw(600))
print(my_account.get_balance())
print(my_account.deposit(250))
print(my_account.withdraw(-500))
print(my_account.withdraw(600))
print(my_account.get_balance())