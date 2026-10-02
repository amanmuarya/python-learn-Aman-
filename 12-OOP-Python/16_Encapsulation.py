"""Definition

Encapsulation means bundling data (variables) and methods (functions) together inside a class and controlling how that data can be accessed or modified."""

#Data ko class ke andar protect karke rakhna aur direct access ko control karna = Encapsulation.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)

account.deposit(500)
print(account.get_balance())