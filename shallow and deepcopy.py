import copy
original=[[1,2],[3,4]]
shallow=copy.copy(original)
shallow[0][0]=99
print(original)


deep=copy.deepcopy(original)
deep[0][0]=19
print(original)
print(deep)

