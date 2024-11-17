lists=[3,4,5,6,7,8]
"""newList = []
for ele in lists:
    newValue = ele ** 3
    newList.append(newValue)
print(newList)"""
mapFunc1=list(map(lambda a: a**3,lists))
mapFunc2=tuple(map(lambda a: a**3,lists))
mapFunc3=set(map(lambda a: a**3,lists))
print(mapFunc1)
print(mapFunc2)
print(mapFunc3)