
import math

def calculate_means(a, b):
    orta_arifmetik = (a + b) / 2
    orta_geometrik = math.sqrt(a * b)
    return orta_arifmetik, orta_geometrik

a = float(input("a sonini kiriting: "))
b = float(input("b sonini kiriting: "))

if a < 0 or b < 0:
    print("O'rta geometrikni hisoblash uchun musbat sonlar kerak.")
else:
    arifmetik, geometrik = calculate_means(a, b)
    print(f"O'rta arifmetik: {arifmetik}")
    print(f"O'rta geometrik: {geometrik}")



