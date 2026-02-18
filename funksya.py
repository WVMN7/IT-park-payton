



# def toliq_ism_yasa(ism, familya):
#     """to'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism}  {familya}"
#     return toliq_ism # 
# talaba1 = toliq_ism_yasa('olim', 'husanov')
# talaba2 = toliq_ism_yasa('husanov', 'olim')
# talaba3 = toliq_ism_yasa('Adham' , 'Ibrogimov')
# print(f"darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"darsga kelgan talaba : {talaba3}")



# def toliq_ism (ism, familya , otasining_ismi = None):
#     talaba = {
#     'ism' : ism,
#     'familya': familya,
#     'otasining_ismi' : otasining_ismi
#     }
#     return talaba1
# talaba2 = toliq_ism('adham', 'Ibrogimovich')
# talaba3 = toliq_ism('adham', 'Ibrogimovich', 'davronovich')
# for talaba1 in talaba2, talaba3:
#     if talaba1['otasining_ismi']:
#         otasining_ismi = talaba1[otasining_ismi]
#     else:
#         otasining_ismi = "nomalum"
#     print(f"talaba1 ['ism']")

# def toliq_ism(ism, familya, otasining_ismi=None):
#     talaba = {
#         'ism': ism,
#         'familya': familya,
#         'otasining_ismi': otasining_ismi
#     }
#     return talaba

# # Talabalar ma'lumotlarini yaratish
# talaba2 = toliq_ism('Adham', 'Ibrogimovich')
# talaba3 = toliq_ism('Adham', 'Ibrogimovich', 'Davronovich')

# # Har bir talaba uchun malumotlarni chiqarish
# for talaba in [talaba2, talaba3]:
#     if talaba['otasining_ismi']:
#         otasining_ismi = talaba['otasining_ismi']
#     else:
#         otasining_ismi = "nomalum"
#     print(f"{talaba['ism']} {talaba['familya']} - Otasining ismi: {otasining_ismi}")


# def oraliq(min, max, qadam):
#     sonlar = []
#     while min < max:  
#         sonlar.append(min)

#         min += 1
#     return sonlar
# print(oraliq(0,10,2))
# print(oraliq(10,21))


# def dostlar (ism, familya,yosh, ** malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familya'] = familya
#     malumotlar['yosh'] = yosh
    
#     return malumotlar
# dost1 = dostlar("Bobur", "Hayitboyev",18, yil = 2006,  )
# dost2 = dostlar("Jamol", "Sultonboyev",19,yil = 2005,  )
# for dost in [dost1,dost2]:
#     print(dost)


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")    
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#            break
#     return avtolar

# def info_print(avtolar):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}")


# import textwrap
# def zed():
#     with open ("pi_million_digits (1).txt") as pi:
#         data = textwrap.load(pi)
    
        
tkun = '86'
with open ('pi_million_digits (1).txt') as w:
    pi = w.read()
print(tkun in pi)

