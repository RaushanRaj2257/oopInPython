class Fraction:
    def __init__(self,d,n):
        self.den=d
        self.num=n
    def __str__(self):
        return "{}/{}".format(self.den,self.num)
    def __add__(self,other):
        temp_num=self.num*other.den+other.num*self.den
        temp_den=self.num*other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self,other):
        temp_num=self.num*other.den-other.num*self.den
        temp_den=self.num*other.den
        return "{}/{}".format(temp_num,temp_den)

    
    
    

a=Fraction(2,5)
b=Fraction(5,8)
print(a)
print(b)
print(a+b)
print(a-b)
