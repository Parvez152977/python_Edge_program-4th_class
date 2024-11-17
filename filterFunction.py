lists=[3,4,5,6,7,8,0]
mapFunc1=list(filter(lambda a: a%2==0 and a!=0,lists))
mapFunc2=tuple(filter(lambda a: a%2!=0,lists))
mapFunc3=set(filter(lambda a: a==0,lists))
print(mapFunc1)
print(mapFunc2)
print(mapFunc3)