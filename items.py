#   .items()- metodi
'''
talaba_0 = {
     'ism': 'alijon',
     'familya': 'yusupov',
    'yoshi': 20 ,
     'fakulteti': 'infarmatika'
     }
#print(talaba_0.items())
for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")

telefonlar = {
    'Ali':'iphone 16',
    'Vali': 'mi10 pro',
    'Asad': 'nokia 1110',
    'Adham': 'honor'
}
for k , q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

mevalar = {
    'olma': '10000',
    'uzum ': '13000',
    'anor': '15000'
}
for k, q in mevalar.items():
    print(f"Bizning do'konda {k.title()} {q} so'm")

#  Keys() - metodi lug'atdagi kalit so'zlarni chiqarib beradi. 
mevalar = {
    'olma': '10000',
    'uzum ': '13000',
    'anor': '15000',
    'tarvuz' : '3000',
    'anjir': '20000'
}
#print(mevalar.keys())

print("Dokondagi mahsulotlar")
for meva in mevalar.keys():
    print(meva)

telefonlar = {
    'redmi': 'mi10 pro',
    'iphone':'16 pro max',
    'infinix' : '20 pro',
    'nokia' : 'mokia 1110'
}
print('Dokonnning maxsulotlari')
for telefon in telefonlar.keys():
    print(telefon)
 '''  
 