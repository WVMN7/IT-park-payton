#     while - toki
'''
son = 0
while son<1000000000000000000000:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)

## INPUT() WHILE

# input

##ism = input('Ismingiz nima? ')
##savol = f"Salom, {ism.title()}. Yoshingiz nechada? "
##yosh = input(savol)
##height = input('Bo\'yingiz necha metr? ')
##height = float(height)

## while - toki

##son = 1 # son ga 1 qiymatini beramiz
##while son<=5: # toki son 5 dan kichik yoki teng ekan...
##    print(son, end=' ') # son ni konsolga chiqaramiz,
####    son = son+1 # songa 1 qo'shamiz.
##    son += 1


##print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
##savol = "Istalgan son kiriting "
##savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
##qiymat = ''
##while qiymat != 'exit':
##    qiymat = input(savol)
##    if qiymat != 'exit':
##        print(float(qiymat)**2)
##print('Dastur tugadi')


## Ishora (flag)

##print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
##savol = "Istalgan son kiriting "
##savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
##ishora = True
##while ishora:
##    qiymat = input(savol)
##    if qiymat == 'exit':
##        ishora = False
##    else:
##        print(float(qiymat)**2)
##print('Dastur to\'xtadi')


## Dasturni to'xtatish usullaridan biri BREAK OPERATORI

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True: # abadiy tsikl
   qiymat = input(savol)
   if qiymat == 'exit':
       break # tsiklni to'xtatish
   else:
       print(float(qiymat)**2)
print('Dastur tugadi')


##sonlar = list(range(1,11))
##for son in sonlar: 
##    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
##        continue # break
##    print(f"{son} ning kvadrati {son**2} ga teng")


##son = 0
##while son<10:
##    son += 1
##    if son%2!=0:
##        continue
##    else:
##        print(son)

## abadiy sikl

##son = 0
##while son<10:
####    son += 1
##    if son%2!=0:
##        continue
##    else:
##        print(son)
##    son += 1


son = 1
while son>0: 
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)


'''

'''
#    uyga vazifa
#   1

print("kitob dasturi.")
savol = "Yaxshi ko'rgan kitobingizni kriting "
savol += "(dasturni to'xtatish uchun 'stop' deb yozing): "


while True:
    qiymat = input(savol)
    if qiymat == 'stop':
     break
    else:
        print(qiymat)

print('dastur tugadi')


#  2

'''
running = True

while running:
    user_input = input("Yoshingizni kiriting (dasturni to'xtatish uchun 'exit'/'quit' deb yozing): ")
    if user_input in ['exit', 'quit']:
        print("Dastur tugadi.")
       
        running = False
    elif user_input.isdigit():
        age = int(user_input)
        if age < 7:
            print("Chipta narxi: 2000 so'm.")
        elif 7 <= age < 18:
            print("Chipta narxi: 3000 so'm.")
        elif 18 <= age < 65:
            print("Chipta narxi: 10000 so'm.")
        else:
            print("Chipta bepul.")
    else:
        print("Iltimos, yoshingizni raqam sifatida kiriting yoki 'exit'/'quit' deb yozing.")

'''
#  3

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = int(input(savol))
    if qiymat<=0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
'''






