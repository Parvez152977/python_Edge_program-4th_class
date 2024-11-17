"""maxValue=lambda a,b:a>b
print(maxValue(2,5))"""

"""a=int(input())
b=int(input())
maxValue=("b is greater","a is greater")[a>b]
print(maxValue)"""
maxValue=lambda a,b:"a is greater" if a>b else "b is greater"
print(maxValue(3,4))