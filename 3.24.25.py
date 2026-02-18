
# import math 

# x = int(input("Xona sonini kiriting: "))
# if x > 30 :
#         print("Bunday xonadon yoq")
# else:
#         a = x / 3 
#         h = math.ceil(30)
#         print(f"siz kiritgan xonadon {h} qavatda joylashgan")




# x = int(input("Biror son kiriting:  "))
# n = x - 1 / 2


##def dell(a,n):
##    S = 0 
##    for i in range(n + 1):
##        daraja = 2 * n + i
##        S += (a ** daraja )/( daraja)
##        return S


def son(n):
    y= 0
    for g in range(1, n  + 1):
        y += g * (n - 1)
    return y

        
    












