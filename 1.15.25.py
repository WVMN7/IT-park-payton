#import math
# a = (math.sqrt(64) + math.log2(4) - 2 * math.pi) / (math.log10(1000) + (pow(81, 1/3)))
# print(a)


# s = (((pow(125,1/3)) * math.log10(100) + math.sqrt(16)) / (abs(-4) - math.log2(32) ) * (math.sqrt(16 / 25)))
# print(s)


# x = (((math.sqrt(16)) / (pow(125,1/3)) + (math.log10(1000) - 3 * math.pi)) / ((pow(16,1/4)) / (pow(243,1/5)) + abs(-2)) * (3**2))
# print(x)


# x = (math.sqrt(9 + math.sqrt(77)) + (math.sqrt(9 - math.sqrt(77))))
# print(x)

#  UYGA VAZIFA
import math
#  1
# z = (((math.sqrt(2**4) + math.log2(32) + math.sqrt(25) / pow(8,1/3) - math.log10(100)) / (abs(-3) + 2 * math.pi)) * (pow(1000,1/3)))
# print(z)

# 2
# x = (((math.sqrt(16)) / (pow(125,1/3)) + (math.log10(1000) - 3 * math.pi)) / ((pow(16,1/4)) / (pow(243,1/5)) + abs(-2)) * (3**2))
# print(x)

# 3
# x = 3.96
# y = 3.58
# z = 2.83
# print(max(x,y,z))
# print(min(x,y,z))


# 4
# x = 0
# y = -4
# z = -1
# print (max(x + y + z , x , y , z))
# print(min(x + y / 2, x , y , z)*min(x + y / 2, x , y , z))


# #  5
# x = 4 
# a = 1.28
# tt = ((math.sqrt(x - 1) + math.sqrt(x + 2) + math.log10((math.sqrt(a * (x **2 + 2))))) / (math.sqrt(math.sqrt(x + 2) + math.sqrt(x + 24) + x**5)))
# print(tt)



x = 4
a = 1.28
TT = ((math.sqrt(x-1) + math.sqrt(x+2) + math.log10(math.sqrt(a * (x**2) + 2))) /
      pow(math.sqrt(x+2) + math.sqrt(x+24) + (x**5) , 1/2))
print(TT)