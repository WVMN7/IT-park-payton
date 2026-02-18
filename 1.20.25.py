# from trans import to_cyrillic, to_latin
# matn = input("matinni kiriting :")

# if matn.isascii() :
#     print(to_cyrillic(matn))
# else :
#     print(to_latin(matn))

import math

# Masala 1: 
def calculate_expression(x):
    x = 2 * math.tan(x + 2) - math.cos(x + 2)**2
    y = 1 + math.cos(x + 2)**2
    term1 = math.sqrt(x / y)
    term2 = math.sin(x**2) / (x**2 + 3)
    AA = term1 + term2
    return round(AA, 2)

# Masala 2: 
def check_inequality(a, b, c):
    if a < b < c:
        return "YES"
    else:
        return "NO"

# Masala 1 uchn giruvchi qiymatla
x_values = [8.38, 8.2]
for x in x_values:
    print(f"x = {x}, AA = {calculate_expression(x)}")

# Masala 2 uchn giruvchi qiymatla
test_cases = [(2, 4, 2), (0, 1, 5)]
for a, b, c in test_cases:
    print(f"a = {a}, b = {b}, c = {c}, Result = {check_inequality(a, b, c)}")
    
