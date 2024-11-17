from functools import reduce

lists=[3,4,5,6,7,8,4]
reduceValue = reduce(lambda a,b: a+b,lists)
print(reduceValue)