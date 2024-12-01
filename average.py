class Student:
    average=0.0
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        self.average=(self.m1+self.m2+self.m3)/3
    def print_data(self):
        self.avg()
        print("Name=",self.name)
        print("Average=",self.average)

s1=Student("Raushan",96,95,91)
s1.print_data()