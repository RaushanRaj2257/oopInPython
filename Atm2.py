

class Atm:
    def __init__(self, balance,pin=None):
        self.__balance=balance
        if pin==None:
            pass
        else:
            self.__pin=pin
        
    

s=Atm(50000)
print(s._Atm__pin)
print(s._Atm__balance)
