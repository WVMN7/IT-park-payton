
##import json
##x = 10 
##
##x_json = json.dumps(x)
##
##y = 3.8
##
##y_json = json.dumps(y)

##m = True
##m_json = json.dumps(m)


##sonlar = (12,34,76,87,54)
##son = json.dumps(sonlar)

##
##bemor = {
##    "ism": "Asad Valiyev",
##    "yosh": 30,
##    "oila": True,
##    "farzandlar": ["Adham","Ali"],
##    "allergiya": None,
##    "dorilar": [
##        {"nomi":"Analgin", "miqdori": 0.5},
##        {"nomi":"Panadol", "miqdori": 1.2}
##        ]
##    }
####bemor_j = json.dumps(bemor,indent = 4)
##with open ('bemor3.json','w') as f:
##    json.dump(bemor,f)
##
##filename = 'bemor.json'
##with open (filename) as d:
##    bemor = json.load(d)
##
####print(bemor)



##
##maktab = {
##    "mnomi": "umumiy orta ta'lim",
##    "son":19,
##    "qavat": 3,
##    "ixtisoslashgan": None,
##    "o'quvchi o'qidi": 675
##    }
##m_json = json.dumps(maktab,indent = 3)
##with open ('maktab.json','w') as m:
##    json.dump(maktab,m,indent= 3)



#   № 1
##data = {
##    "model": "Malibu",
##    "Rang": "Qora",
##    "yil": 2020,
##    "narx":40000
##    }
##jso = json.dumps(data,indent = 3)
##with open ('data.json','w') as dw:
##    json.dump(data,dw,indent = 3)

##-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##                                                                          2.21.25y
##yosh = input("yoshingizni kiriting:")
##yosh = int(yosh)
##print(f"Siz {2025 - yosh} yilda tug'ilgansiz")

##yosh = input("yoshingizni kiriting:")
##try :
##    yosh = int(yosh)
##    print(f"Siz {2025 - yosh} yilda tug;ilgansiz")
##except ValueError:
##    print("dastur ishlab turibdi")
##print("Dastur tugamadi!")
    
##x,y = 5,10
##y/(x-5)



##x,y = 5,10
##try:
##    y/(x-5)
##except ZeroDivisionError:
##    print('0 ga bolinmaydi')

##user = {
##    "username":"Asadov",
##    "status":"Admin",
##    "emeil":"admin@gmail.com",
##    "phone":"+998 97 725 65 15"
##    }
##key = "phone"
##print(f"Foydalanuvchi:  {user[key]}")
##    
##user = {
##    "username":"Asadov",
##    "status":"Admin",
##    "emeil":"admin@gmail.com",
##    "phone":"+998 97 725 65 15"
##    }
##key = "tel"
##try:
##    print(f"Foydalanuvchi:  {user[key]}")
##except KeyError:
##    print("bunday kalit yoq")
##    


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##                                                                                                           2.24.25y

##FileNotFoundError


##import json
##
##files = ['bemor.json','bemor2.json','bemor3.json','bemor4.json']
##for filename in files:
##    try:
##        with open ( filename ) as f:
##            bemor = json.load(f)
##    except FileNotFoundError:
##     #   print(f"{filename} mavjud emas")
##          pass
##    else: 
##        print(bemor['ism'])
##            
##while True:
##    yosh = input("yoshingizni kiriting:  ")
##    if yosh.isdigit():
##        yosh = int(yosh)
##        break
##print(f"Siz {2025  - yosh} yilda tugilgansiz")
##        



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                               2.26.25y


##def get_ful_name(ism, familya):
##    return f"{ism} {familya}".title()
##print(get_ful_name("alijon ","valiyev"))

##def get_ful_name(ism, familya, otasi):
##    return f"{ism} {familya}  {otasi}".title()
##
##
##def get_ful_name(ism, familya, otasi=''):
##    if otasi:
##        return f"{ism}  {familya}  {otasi} ".title()
##    else:
##        return f"{ism} {familya}".title()  
##        

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''                                                                                            2.28.25y                                                                                                                                '''

##def son(a,b,c):
##  return max(a,b,c)
##def sonn(a,b,c):
##  return min(a,b,c)

#                 uyga vazifa
##def bosh_harf (text):
##    print (text.title() )
##
##matn = [title()]


#             1

##def bosh_harf(texts):
##    return [text.capitalize() for text in texts]
##  
##m = ["asad", "rustam", "bekzod", "ali"]
##bbb = bosh_harf(m)
##print(bbb)


#     2

##def juft(x):
##    juftlar = []  
##    for son in x: 
##        if son % 2 == 0:  
##            juftlar.append(son)  
##    return juftlar  
##sonlar = [45,44,66,67,84,25,75,55]
##natija = juft(sonlar)
##print("Juft sonlar:", natija)
##   
     
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##                                                                                                    3.3.25y

##import datetime as dt
##
##hozir = dt.datetime.now()
##print(hozir)

###sanani ajratib olish
##print(hozir.date())
##
###vaqtni ajratib olish
##print(hozir.time())
##
###soatni ajratib olish
##print(hozir.hour)
##
###minutni ajratib olish
##print(hozir.minute)
##
#sekundni ajratib olish
##print(hozir.second)
##
##bugun = dt.date.today()
##print(f"bugungi sana :  {bugun}")

##vaqthozir = hozir.time()
##print(f"hozir soat :  {vaqthozir}")

##bugun = dt.date.today()
##aksiya_vaqti = dt.date(2025, 4, 1)
##farq = aksiya_vaqti - bugun
##print(farq)


##soatlar orasidagi farq
##
##hozir = dt.datetime.now()
##fotbol = dt.datetime(2025,3,3,23,45,00)
##farq = fotbol - hozir
##sekundlar = farq.seconds
##minutlar = int(sekundlar/60)
##soatlar = int(sekundlar/60)
##print(f"footboll boshlanishiga {sekundlar} sekund qoldi")
##print(f"footboll boshlanishiga {minutlar} minut qoldi")
##print(f"footboll boshlanishiga {soatlar} soat qoldi")


##import math
##pi = round(math.pi,2)
##print(f"pining qiymati {pi}")
##
##e = round(math.e,2)
##print(f"e ning qiymati {e}")
#                                         uyga vazifa
######import datetime as dt
####### 1
######hozir = dt.datetime.now()
######ramozon = dt.datetime(2025,3,30)
######farq = ramozon - hozir
######day = farq.days
######print(f"Ramazon tugashiga {day} kun qoldi")
######
####### 2     
######from datetime import datetime, timedelta
######bugun = datetime.today()
######for m in range(10):
######    sana = bugun + timedelta(weeks=2 * m)
######    print(sana.strftime("%Y-%m-%d"))


##def juft_son(x):
##    for z in x:
##     z = []
##     if z % 2 == 0:
##        return z
##son = [22,6,55,44,33,77,99,88]
##javob = juft_son(son)
##print(f"juft sonlar {javob}")
##    

##
##def juft(x):
##
##    for son in x: 
##        if son % 2 == 0:  
##           return juft  
##sonlar = [45,44,66,67,84,25,75,55]
##natija = juft(sonlar)
##print("Juft sonlar:", natija)
   

##def juft(x):
##    juftlar = []  
##    for son in x: 
##        if son % 2 == 0:  
##            juftlar.append(son)  
##    return juftlar  
##sonlar = [45,44,66,67,84,25,75,55]
##natija = juft(sonlar)
##print("Juft sonlar:", natija)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                         3.7.25y
##import json
##filename = 'students.json'
##with open (filename) as w:
##    bemor = json.load(w)
##{"student": [
##    {"id": "01",
##     "name": "Tom",
##     "lastname": "Price",
##     "year": 4, "faculty": "Engineering"},
##    {"id": "02",
##     "name": "Nick",
##     "lastname": "Thameson",
##     "year": 3, "faculty": "Computer Science"},
##    {"id": "03",
##     "name": "John",
##     "lastname": "Doe",
##     "year": 2,
##     "faculty": "ICT"}]}
####import json
####with open ("students.json") as g:
####    data = json.load(g)
####for item in data["student"]:
####    print(f"{item['name']}  {item['lastname]} " f"{item['year']}")
##import json
##with open ("students.json") as g:
##    data = json.load(g)
##for item in data["student"]:
##    return f"{item['name']}  {item['lastname']}"  f" {item['year']} "


import json
with open ("students.json") as f:
    data = json.load(f)
for item in data["student"]:
     print(f"{item['name']}  {item['lastname']}"  f" {item['year']} ")













