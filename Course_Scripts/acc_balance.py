
class Account():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Amount {amount} has been successfully deposited.')
        print(f'Current Account Balance is {self.balance}')

    def withdraw(self, amount):
        if (amount < self.balance):
            self.balance = self.balance - amount
            print(f'Amount {amount} has been withdraw successfully.')
            print(f'Current Account Balance is {self.balance}')
        else:
            print('Insufficent funds in your account')
            print(f'Current Account Balance is {self.balance}')

    def __str__(self):
        return f'Account holder name is {self.name} and Current Account Balance is {self.balance}'


a = Account('Jose', 1000)
print(a)
a.deposit(3500)
a.withdraw(800)
a.withdraw(4000)