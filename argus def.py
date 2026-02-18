# def summa (x,y,* z):
#     """kiritilgan sonlarni yig'indisini hisoblovchi funksiya"""
#     return x +y + sum (z)
# print(summa(2,4,5))


# **kwargs - kaayword arguments (kalit so'zli argumentlar)

# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqida malumotni qaytaruvchi funksiyz"""
#     malumotlar['kompaniya']= kompaniya
#     malumotlar['model']= model
#     malumotlar['narx'] = 15000
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang = 'qora', yil = 2015)
# avto2 = avto_info("Kia", "K5", rang = 'oq', yil = 2022)
# for avto in [avto1, avto2]:
#     print(avto)


# def summa (x,y,* z):
#     """kiritilgan sonlarni yig'indisini hisoblovchi funksiya"""
#     return x / y / sum (z)
# print(summa(2,4,5))



#   uyga vazifa

#   Istalgancha sonlarni qabul qilib, ularning yig'indisini qaytaruvchi funksiya yozing
# 1
# def summa (x,y,* z):
#     """kiritilgan sonlarni yig'indisini hisoblovchi funksiya"""
#     return x + y + sum (z)
# print(summa(2,4,5))

#  2
#  Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing


# def summa (x,y,* z):
#     """kiritilgan sonlarni yig'indisini hisoblovchi funksiya"""
#     return x * y * sum (z)
# print(summa(2,5,3))



#   3
# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy 
# ko'rinishda istalgancha berilishi mumkin bo'lsin.


# def talabalar (ism, familya, ** malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familya'] = familya
    
#     return malumotlar
# talaba1 = talabalar("Abror", "Karimov", yil = 2010,  yosh = 14)
# talaba2 = talabalar("Xasan", "mavlonov",yil = 2005,  yosh = 19)
# for talaba in [talaba1, talaba2]:
#     print(talaba)



#   4
# Do'stingiz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya yozing, 
# Do'stingizni ismi, familyasi va yoshi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy
# ko'rinishda istalgancha berilishi mumkin bo'lsin

# def dostlar (ism, familya,yosh, ** malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familya'] = familya
#     malumotlar['yosh'] = yosh
    
#     return malumotlar
# dost1 = dostlar("Bobur", "Hayitboyev",18, yil = 2006,  )
# dost2 = dostlar("Jamol", "Sultonboyev",19,yil = 2005,  )
# for dost in [dost1,dost2]:
#     print(dost)




