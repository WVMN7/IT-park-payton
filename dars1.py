'''olimp = int(input("Assalomu alaykum Olimp restaraniga xush kelibsiz, niman xarid qilmoqchisiz :"))

if olimp == 'palov':
    print 
'''
'''
narx = 15000
salat = input("Salat olasizmi ?")
non = input("Non olasizmi ?")
asarti = input("Asarti olasizmi ?")
choy = input("Choy olasizmi ?")
suv = input("Suv olasizmi ?")
if salat == "ha" :
  narx = narx + 5000
elif salat == "yoq" :
  narx = narx 
if non == "ha" :
  narx = narx + 3000
elif non =="yoq" :
  narx = narx 
if asarti == "ha" :
   narx = narx + 5000
elif asarti == "yoq" :
   narx = narx 
if choy == "ha" :
   narx = narx + 2000
elif choy == "yoq" :
   narx = narx 
if suv == "ha" :
   narx = narx + 5000
elif suv == "yoq" :
   narx = narx 
print('salat')
print('non')
print("asarti")
print("choy")
print("suv")
print(f"sizdan {narx} som")
'''
# Dictionary - Lug'atlar
#   key - kalit so'zi: qiymat  
#car = {'model': 'Gentra', 'rang': "qora"}
#print(car['model'])
#Uyga vazifa
#1
'''
oilam = {'otam': "Xudayberganov Jalolbek", 'onam': "Xajiyeva Maqsuda",\
'akam': "Sobiryozov Jahongir", 'men': "Sobiryozov Abbosbek"}
print(f"Otamning ismi {oilam['otam']},1983-yil Xorazm viloyatida tug'ilgan")
print(f"Onamning ismi {oilam['onam']},1982-yil Xorazm viloyatida tug'ilgan")
print(f"Akamning ismi {oilam['akam']},2007-yil Xorazm viloyatida tug'ilgan")

#   2
dostlar = {"Ali": "osh", "Javohir": "pitsa", "Sulaymon": "shorva", "Mirjahon": "qovurdoq", "adham": "burger"}
print(f"Javohirning sevimli taomi {dostlar['Javohir']}")
print(f"Sulaymonning sevimli taomi {dostlar['Sulaymon']}")
print(f"Mirjahonning sevimli taomi {dostlar['Mirjahon']}")

#   3
python = {"if": "agar degan manoni anglatadi", "else": "aks holda degan manoni anglatadi\
", "elif": "aks holda degan manoni anglatadi", "upper": "hamma harflarni katta bilan yozadi",\
"title": "bosh harfini katta bilan yozadi"}
print(f"if - {python['if']}")
print(f"else - {python['else']}")
'''
#  4
'''
sozlar = {"apple": "olma", "flight": "jang", "shadow": "soya"}
javob = input("so'zni kriting :")
#javob = sozlar.get('black'),"bunday soz yoq"
#print(javob)
'''
izohli_lugat ={
   "apple":"olma",
   "banana": "banan",
   "apricot":"o'rik",
   "tomato": "pomidor"
}
kalit = input("kalit so'zni kriting: ") .lower()
#print(izohli_lugat.get(kalit ,"bunday so'z mavjud emas"))


kalit = input("kalit so'zni kriting: ") .lower()
tarjima = izohli_lugat.get(kalit)
if tarjima ==None:
   print("kalit so'zinin kriting")
else:
   print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
























