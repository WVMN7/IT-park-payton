##3.17.25 yil

##
##import math
##a = int(input("a: sonini kiriting >> ")) 
##b = int(input("b: sonini kiriting >> "))
##c = int(input("c: sonini kiriting >> "))
##d = b**2 - 4 * a**4 * c
##if d == 0:
##    x = -b / 2 * a
##    print(x)
##elif d > 0:
##    z = (-b-math.sqrt(d)) / (2 *a)
##    c = (-b+math.sqrt(d)) / (2 *a ) 
##    print(z,c)     
##else:
##    print('No')


##import math
##def  bikvadrat(a,b,c):
##    D = b**2 - 4 * a * c
##    if D < 0 :
##        return "Ildizlari"
##    t1 = (-b + math.sqrt(D)) / (2 ** a)
##    t2 = (-b - math.sqrt(D)) / (2 ** a)
##
##    ildizlar = set()
##
##    for x in (t1, t2):
##        if x >= 0:
##            ildizlar.add(math.sqrt(x))
##            ildizlar.add(math.sqrt(x))
##
##    if ildizlar:
##        return f"ildizlari {t1,t2}"
            
        
import math

a = int(input('a sonini kiriting >>> '))
b = int(input('b sonini kiriting >>> '))

orta_arf = (a + b) / 2
orta_geom = math.sqrt(a * b)
print(f"{a} va {b} ning o'rta arifmetik qiymati: {orta_arf}")
print(f"{a} va {b} ning o'rta geometrik qiymati: {orta_geom}")
















