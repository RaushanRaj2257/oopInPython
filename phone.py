class Product:

    def __init__(self):
        print("Product constructor")
    
    def buy(self):
        print("Buying product")

class Phone:

    def __init__(self):
        print("Phone constructor")
    
    def buy(self):
        print("buying phone")
    
class SmartPhone(Phone,Product):
    pass


s=SmartPhone()
s.buy()