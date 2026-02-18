#'''
#cars = []
#for  n in range(15) : 
#    new_car = {
#        "model": None , 
#        "rang": None , 
#        "yil": None ,
#        "km": None ,
#        "narx": None, 
#        "karobka": None
#    }
#    cars.append(new_car)
#for car in cars [:4] :
#    car['model'] = 'cobalt'
#    car['rang'] = 'qizil'
#    car['yil'] = 2020
#    car['km'] = 5000
#    car['karobka'] = 'avto'
#
#for car in cars [4:9] :
#    car['model'] = 'gentra'
#    car['rang'] = 'qora'
#    car['yil'] = 2018
#    car['km'] = 5500
#    car['karobka'] = 'mexanik'
#
#for car in cars [9:15] :
#    car['model'] = 'nexia 2'
#    car['rang'] = 'oq'
#    car['yil'] = 2021
#    car['km'] = 4000
#    car['karobka'] = 'avto'
#
#for car in cars :
#    if car ['karobka'] == "avto" :
#        car['narx'] = 40000
#    else:
#        car['narx'] = 37000
#
#for car in cars :
#    print(car)
#''
'''
mashinalar = {
    'cobalt' : 'avtomat',
    'nexia 3': 'mexanik' ,
    'malibu': 'avtomat' 
}

for ism, til in mashinalar.items():
    print(f"\n{ism.title()} avto mashinasi {til} karobka ")


#      uyga vazifa
'''
'''
dostlar = {
    'Ali': ['Tuman ' , 'Terminator', 'Karatechi bola'] ,
    'Sardor': ['Trasformerlar' , 'Suniy ong', 'Kobra kai'] ,
    'Azamat': ['Garri poter', 'Intrsteller', "O'rgimchak odam"]
}
#for dost in dostlar:
#    print("Alining yoqtirgan kinosi:  ")
for k , q in dostlar.items():
    print(f"{k.title()}ning sevimli kinosi:\n {q}")
'''
ilm_fan = {
    'ism': 'Povel Duruf',
    'yili': '1984 yil' , 
    'sohasi':  'dasturchi'
}
