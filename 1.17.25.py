import math
# a = 0.36
# b = 1.02
# t =  pow(a, 1/5) + (pow(b * ((a + b) / (2 * b + a * b)) ,1/4)) * (((a**2) + (b**2) + 2))
# print(round(t ,2))



# x = 9.79
# y = 6.74
# c = (x + y) / (y**2) + abs((y**2 + 2)) / x + (x**3/5) + pow(math.e,(y +2))
# print(round(c, 2))

x = 1
y = 1.84
z = 0.53
af =  1/pow(x,-2) * math.sqrt(x + pow(abs(y) + 2) ,1/4) * pow(math.e,(x - 1) / math.sin(z + 2) +2, 1/3)
print(round(af,2))


