# a = int(input("birinchi sonni kiriting >>> "))
# b = int(input("ikkinchi sonni kiriting >>> "))

# print(min(a,b) * max(a,b))
# print(a + b)



# N = int(input("N sonini kiriting >>>  "))

# if N % 2 ==0 and N % 3 == 0:
#     print("Bu son 2 va 3 ga qoldiqsiz bo'linadi.")
# elif N % 2 ==0 :
#     print("bu sonfaqat 2 ga bolinadi")
# elif N % 3 == 0:
#     print("bu son faqat 3 ga qoldiqsiz bolinadi")
# else:
#     print("Bu son 2 ga ham 3 ga ham bo'linmaydi")



# a = int(input("birinchi sonni kiriting >>> "))
# b = int(input("ikkinchi sonni kiriting >>> "))
# c = int(input("uchinchi sonni kiriting >>> "))

# if (a,b,c) and (a,b,-c) and (-a,b,c) and (a,-b,c):
#     print(a + b + c )
# elif (-a,-b,-c) and (a,-b,-c) and (-a,b,-c) and (-a,-b,c):
#     print(a * b * c)


# a1 = int(input("a1 ni kiriting >>>"))
# b1 = int(input("b1 ni kiriting >>>"))
# a2 = int(input("a2 ni kiriting >>>"))
# b2 = int(input("b2 ni kiriting >>>"))

# kasr_surati = a1 * b2 + a2 * b1
# kasr_maxraji = b1 * b2

# print(f"javob : {kasr_surati} / {kasr_maxraji}")



#   UYGA VAZIFA
#      1
import math
a = int(input("a sonini kiriting: >>> "))
b = int(input("b sonini kiriting: >>> "))
x = int(input("x sonini kiriting: >>> "))


T = (pow(a + 1,1/3)) + (math.sqrt((a * (x **2) + 2 * b) /( 2 * b + a * b))) * (a + (x ** 2) + 2 * (b ** 2))
javob = round(T)
print(f"bu misolning javobi: >>> {javob}")

#    2

def err (x,y):
   a = (x + 2 * y) / ((y ** 2) + abs(((y**2) + 2) / (x + 1))) + (2 * y - y)
   javob = (round(a))
   print(f"bu misolning javobi: >>>> {javob}")

