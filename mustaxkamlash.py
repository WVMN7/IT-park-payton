# '''
# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n = 1
# while True:
#     savol = f"{n} - do'stingizni ismini kriting:"
#     ism =input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi ?  (ha/yoq)")
#     if javob =="ha":
#         n += 1
#         continue
#     else:
#         break

# print("do'slaringizni ro'yxati:")
# for ism in ismlar:
#      print(ism.title())
# '''

# print("Do'stingizni yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kriting:")
#     yosh = input("Do'stingizni yoshini kriting:")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yoq)")
#     if javob == "yoq":
#       ishora = False

# for ism, yosh in dostlar.items():
#    print(f"{ism.title()} {yosh}" )

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar :
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kriting:")
#     print(f"{talaba}")



# #      uyga vazifa

# #   1
# buyurtmalar = []
# while True:
#     mahsulot = input("Mahsulot nomini kiriting (dasturni to'xtatish uchun 'stop' deb yozing): ")
#     if mahsulot == 'stop':
#         break
#     buyurtmalar.append(mahsulot)
# print("\nBuyurtmalar ro'yxati:")
# for index, mahsulot in enumerate(buyurtmalar, 1):
#     print(f"{index}. {mahsulot}")
      
# #  2

# bozor = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting (yoki 'stop' deb yozing to'xtatish uchun): ")
#     if mahsulot == 'stop':
#         break
#     try:
#         narh = float(input(f"{mahsulot} mahsuloti uchun narhni kiriting: "))
#         bozor[mahsulot] = narh
#     except ValueError:
#         print("Iltimos, narhni son sifatida kiriting.")
# print("\nE-bozor mahsulotlari va narxlari:")
# for mahsulot, narh in bozor.items():
#     print(f"{mahsulot}: {narh} so'm")

# royhat = {"gosht" : 75000 , "tovuq" : 35000 , "yog'" : 20000 , "un" : 255000}
# print("EBozor dastavka hizmatiga xush kelibsiz")
# savol = input("Nima dastavka qilmoqchisiz")
# if royhat or savol :
#     print("dastavka manzilga boradi")
# elif royhat != savol :
#     print("kechirasiz bizda bu maxsulot yo'q")
    

















