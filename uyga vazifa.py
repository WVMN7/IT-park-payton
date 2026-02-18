#    uyga vazifa
#   1
# def toliq_ism (ism,familya,tugilgan_yili,e_manzili,tel_raqam ):
#     malumot = {
#         "ism": ism , 
#         "familya": familya,
#         "tugilgan_yili": tugilgan_yili,
#         "e_manzili": e_manzili,
#         "tel_raqam": tel_raqam
#     }
#     return malumot
# malumot1 = toliq_ism('Odil','Yoqubov','1994','odilyoqubov@gmail.com','97 243 43 23')
# malumot2 = toliq_ism('Bobur','Kamilov','2001','bkamilov@gmail.com','98 543 54 74')
# for malumot in [malumot1, malumot2]:
#     print(malumot)

#  3

# def eng_katta_son(a, b, c):
#     return max(a, b , c)

# son1 = int(input("Birinchi sonni kiriting:"))
# son2 = int(input("Ikkinchi sonni kiriting:"))
# son3 = int(input("Uchinchi sonni kiriting:"))
# print("Eng katta son:", eng_katta_son(son1, son2, son3))


#  4

import math

def aylana ():
    """Aylanani peremetri va yuzini hisoblovchi funksiya"""
r = int(input("aylanani radyusini kiriting:"))
diometr = r * 2
peremetr = 2 * math.pi * r
yuza = math.pi * r ** 2
print(f"Aylanani radiusi {r}ga teng\nAylanani diometri
       {diometr}ga teng\nAylanani peremetri {peremetr}ga teng\nAylanani
         yuzi {yuza}ga teng")









#   uyga vazifa

#   Istalgancha sonlarni qabul qilib, ularning yig'indisini qaytaruvchi funksiya yozing
