# x = int("birinchi sonni kriting: ")
# y = int("ikkinchi sonni kriting: ")
# z = int("uchinchi sonni kriting: ")

# x = 0,43
# y = 1,11
# z = 0,75


# if x < 1 and y < 1 and z < 1:
#     eng_kichik = min(x,y,z)
#     eng_kichik = y + z/2
#     print(eng_kichik)
# else: 
#     print(x,y,z)

# x = 0.43
# y = 1.11
# z = 0.75
# if x <1 and y<1 and z<1:
#     eng_kichigi = min(x,y,z)
#     eng_kichigi = y+z/2
#     print(eng_kichigi)
# else:
#     print(x,y,z)




##def w(x,y,z):
##    if x < 1 and y < 1 and z < 1:
##        kichik = min(x,y,z)
##        y_yigindi = (x + y + z - kichik) / 2
##
##        if kichik == x:
##            x = y_yigindi
##        elif kichik == y:
##            y = y_yigindi
##        else:
##            z = y_yigindi
##    return (x,y,z)

##def rim(a,b,c,d):
##    if a <= b <= c <=d:
##        katta = max(a,b,c,d)
##        a = katta
##        b = katta
##        c = katta
##        d = katta
##        return a,b,c,d
##    else:
##        kichik = min(a,b,c,d)
##        a = kichik 
##        b = kichik
##        c = kichik
##        d = kichik
##        return a,b,c,d
        
## Uyga vazifa
##        1 
##import math
##def win (x,y):
##    if x < 0 and y < 0 :
##        x,y = abs(x), abs(y)
##        return x,y
##    elif x > 0 and y < 0 :
##        c = x + 0.5 , y + 0.5
##        return c
##    elif x < 0 and y > 0:
##        b = x + 0.5 , y + 0.5
##        return b
##    else:
##        return x,y
    
##         2
x = int(input("a sonini kiriting:  "))
y = int(input("y sonini kiriting:  "))
z = int(input("z sonini kiriting:  "))
if x+y>z :
    print('YES')
    if x+z>y :
           print('YES')
    elif y+z>x :
           print('YES')
else:
       print('NO')

# import math
# a = int(input("a: sonini kiriting >> "))
# b = int(input("b: sonini kiriting >> "))
# c = int(input("c: sonini kiriting >> "))
# d = b**2 - 4 * a * c
# if d == 0:
#     x = -b / 2 * a
#     print(x)
# elif d > 0:
#     z = (-b-math.sqrt(d)) / (2 *a)
#     c = (-b+math.sqrt(d)) / (2 *a ) 
#     print(z,c)     
# else:
#     print('No')

# a = int(input("a : sonini kiriting: >> "))
# b = int(input("b : sonini kiriting: >> "))
# c = int(input("c : sonini kiriting: >> "))

# if (a,b,c ) > 0:
#     a,b,c = (a**2), (b**2), (c**2)
# else:
#     print(a,b,c)


















