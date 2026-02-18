# def salom_ber(): 
#     """Salom beruvchi funksya"""
#     print(salom_ber)
# salom_ber()


# def salom_ber (ism):
#     """foydalanuvchi ismini qabul qilib unga salom beruvchi dastur"""
#     print(f"Assalomu alaykum hurmatli {ism.title()}")
# salom_ber('ilhom')
# salom_ber('hasan')
# print(salom_ber.__doc__)
# print(print.__doc__)



# def toliq_ism(ism, familya):
#     """foydalanuvchini toliq ism familyasini qabul qiluvchi dastur"""
#     print(f"foydalanuvchini ismi: {ism.title()}\n "
#           f"foydalanuvchini familyasi: {familya.title()}")
# toliq_ism('olim', 'husanov')
# toliq_ism('husanov', 'olim')



# def yosh_hisobla(ism, tuglgan_yil):
#     """foydalanuvchini yoshini hisoblavchi funksiya"""
#     print(f"{ism.title()} , {2024 - tuglgan_yil} yoshda")

# yosh_hisobla('hasan', 1992)



# def son_darajasi(son):
#     """sonni kvadrati va kubini hisoblovchi funksiya"""
#     print(f"{son} sonning kvadrati {son**2} ga , kubi {son**3} ga teng")
# # son_darajasi(5)
    

# def qoldiq(son):
#     """sonni qoldiqsiz bolinadigan son funksiyasi"""
# def qoldiqsiz_boladigan_sonlar(n):
#     # 1 dan n gacha bo'lgan sonlarni tekshiramiz
#     for i in range(1, n+1):
#         if n % i == 0:  # Agar n i ga qoldiqsiz bo'linadigan bo'lsa
#             print(i)

# # Foydalanuvchidan sonni olish
# son = int(input("Son kiriting: "))
# qoldiqsiz_boladigan_sonlar(son)




# def bolinish_alomati(son):
#     """foydalanuvchikiritgan sonni kvadrati va kubinihisoblovchi funksiya"""
#     for n in range(2,11):
#         if not son%n :
#             print(f"{son}  {n} songa qoldiqsiz bolinadi")
# bolinish_alomati(49)



#      uyga vazifa

# def katta_sonni_top():
#     """Sonlarni taqqoslovchi funksiya"""
#     son1 = float(input("Birinchi sonni kiriting: "))
#     son2 = float(input("Ikkinchi sonni kiriting: "))
    
#     if son1 == son2:
#         print("Sonlar teng")
#     else:
#         print(f"Kattasi: {max(son1, son2)}")

# katta_sonni_top()




# def daraja_hisobla():
#      """Sonni darajasini hisoblovchi funksiya"""
# x = float(input("X sonini kiriting: "))
# y = float(input("Y sonini kiriting: "))
    
# print(f"{x} ning {y} - darajasi: {x ** y}")

# daraja_hisobla()



# takrorlash

# def tugilgan_yil():
#     """odamni nechanchi yil ekanlikini hisoblovchi funksiya"""
# ism = input("Ismingizni kiriting:")
# yosh = int(input("Yoshingizni kiriting:"))
# print(f"Siz {ism}, yoshingiz {yosh} da, yilingiz {2024 - yosh} ")

# tugilgan_yil()



son = input("Biror son kriting:")
def sonlar():
    """sonlarni toq yoki juft ekanligini hisoblovchi funksiya"""
    if son % 2 == 0:
        print('Son juft')
    else:
        print('son toq')
sonlar()
