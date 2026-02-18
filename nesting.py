#  NESTING - bir narsani ichida boshqa narsani joylash
'''
car0 = {
    "model": "locetti",
    "rang": "oq rang",
    "yili": 2018 ,
    "narx": 15000,
    "km": 5000 , 
    "karobka": "mexanik"
}
car1 = {
    "model": "gentra",
    "rang": "qora rang",
    "yili": 2019 ,
    "narx": 20000,
    "km": 8000,
    "karobka": "avtomat"
}
car2 = {
    "model": "Nexia 3",
    "rang": "oq rang",
    "yili": 2020 ,
    "narx": 13000,
    "km": 5000,
    "karobka":"mexanika"
}
cars = [car0, car1, car2]
#for car in cars:
  #  print(f"{car['model'] .title()} , {car['rang']}, {car['yili']} yil, {car['narx']}$, {car['km']}km yurgan, {car['karobka']}")
#print(cars[2])
#print(cars[0]['model'])   
print(f"{cars[2]['model'] .title()} , {cars[2]['rang']}")  
'''
'''
malibus = []
for n in range(10) :
    new_car = {
        "model": "malibu", 
        "rang": None,
        "yil": 2024,
        "narx": None,
        "km": 0,
        "karobka": "avto"
              }
    malibus.append(new_car)
for malibu in malibus [:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus [3:6]:
    malibu['rang'] = 'qora'

for molibu in malibus:
    if malibu['karobka'] =='avto':
        malibu['narx'] = 40000
    else:
        malibu['narx'] = 35000

for malibu in malibus:
    print(malibu)
'''
import calendar
yy = 2024
mm = 11
print(calendar.month(yy ,mm))