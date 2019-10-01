import math

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
if a < b + c and b < a + c and c < a + b:
    print('This is triangle')
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('S=', S)
else:
    print('Incorrect params')
