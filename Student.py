class Student:
    def __init__(self, name):
        self.name=name

    def print_name(self):
        print("Hi,",self.name)


s1=Student("Raushan Raj")
s1.print_name()