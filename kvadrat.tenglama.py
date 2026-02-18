import math
a = int(input("a: sonini kiriting >> "))
b = int(input("b: sonini kiriting >> "))
c = int(input("c: sonini kiriting >> "))
d = b**2 - 4 * a * c
if d == 0:
    x = -b / 2 * a
    print(x)
elif d > 0:
    z = (-b-math.sqrt(d)) / (2 *a)
    c = (-b+math.sqrt(d)) / (2 *a ) 
    print(z,c)     
else:
    print('No')