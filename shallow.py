import copy

s=[[1,2],[3,4]]
print(s)
print(id(s))

c=copy.copy(s)
print(c)
print(id(c))