class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    @property
    def percentange(self):
        return (self.phy+self.chem+self.math)/3
    
std1=Student(98,97,99)
print(std1.percentange)
std1.chem=79
print(std1.percentange)

