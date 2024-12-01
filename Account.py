class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    def debit(self,amount):
        self.balance=self.balance-amount
        print("Debited Successfully")

    def credit(self,amount):
        self.balance=self.balance+amount
        print("Credit Successfully")

    def check_Balance(self):
        print("your Balance is ",self.balance)



a1=Account(15000,152000123)
a1.check_Balance()
a1.debit(12000)
a1.check_Balance()
a1.credit(15000)
a1.check_Balance()