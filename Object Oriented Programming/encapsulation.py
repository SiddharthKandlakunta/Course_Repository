#It is the practice of bundling data and the methods that operate on that data inside a class, while controlling access to the data


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    @property
    def get_balance(self):
        return self.__balance
    
account = BankAccount(10000)
account.deposit(5000)
account.withdraw(2000)
#account.__balance = 10000

print(account.get_balance)