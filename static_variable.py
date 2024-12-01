class Atm:
    counter=1
    def __init__(self):
        self.sno=Atm.counter
        Atm.counter+=1

c1=Atm()
c2=Atm()
c3=Atm()
c4=Atm()
c5=Atm()
print(c1.sno)
print(c2.sno)
print(c3.sno)
print(c4.sno)
print(c5.sno)