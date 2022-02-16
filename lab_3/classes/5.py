class Account:
    person = ' '
    balance = 0
    def __init__(self, person, balance):
        self.person = person
        self.balance = balance 
    def show(self):
        return f'Account person: {self.person} \nAccount balance: {self.balance}'
    def deposit(self, cnt):
        self.balance = self.balance + cnt
        return f'Refreshed balance: {self.balance}'
    def withdraw(self, cnt):
        if cnt <= self.balance:
            self.balance = self.balance - cnt
            return f'Remaining balance: {self.balance}'
        return f'This action cannot be done, because you don not have enough money'
        exit()
        

account = Account("Aigerim Khamit", 10000000)
print(account.show())
print(account.deposit(1500000))
print(account.withdraw(7000000))
print(account.deposit(8000000))
print(account.withdraw(20000000))

