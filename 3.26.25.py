##svitafor = 'qizil'
##
##match svitafor:
##    case 'qizil':
##        print("To'xtab tur")
##    case 'sariq':
##        print("Tayyorlan")
##    case 'yshil':
##        print("Hayda")

##
##hafta = 1
##match hafta:
##    case 1:
##        print("Dushanba")
##    case 2:
##        print("Seshanba")
##    case 3:
##        print("Chorshanba")
##    case 4:
##        print("Payshanba")
##    case 5:
##        print("Juma")
##    case 6:
##        print("Shanba")
##    case 7:
##        print("Yakshanba")



##hafta_kunlari = 2
##match hafta_kunlari:
##    case 1:
##        print('Dushanba')
##    case 2:
##        print('Seshanba')
##    case 3:
##        print('Chorshanba')
##    case 4:
##        print('Payshanba')
##    case 5:
##        print('Juma')
##    case 6:
##        print('Shanba')
##    case 7:
##        print('Yakshanba')


##
##gg = oktyabr
##match gg:
##        case 'sentyabr' | 'oktyabr' | 'noyabr':
##            print("hozir kuz fasli")
##        case 'dekabr' | 'yanvar' | 'fevral' :
##            print("hozir qish fasli")
##        case 'mart' | 'aprel' | 'may':
##            print("hozir bahor fasli")
##        case 'iyun' | 'iyul' | 'avgust':
##            print("hozir yoz fasli")





##def fasl(oy):
##    match oy:
##        case 'Dekabr' | 'Yanvar' | 'Fevral':
##            print("Hozir qish.")
##        case 'Mart' | 'Aprel' | 'May':
##            print("Hozir bahor.")
##        case 'Iyun' | 'Iyul' | 'Avgust':
##            print("Hozir yoz.")
##        case 'Sentabr' | 'Oktabr' | 'Noyabr':
##            print("Hozir kuz.")
##        case _:
##            print("Bunday oy mavjud emas!")

##def baho(dd):
##    match dd:
##        case 5:
##            print('Alo')
##        case 4:
##            print('yaxshi')
##        case 3 :
##            print('qoniqarli')
##        case 2:
##            print('qoniqarsiz')
##        case 1:
##            print('juda yomon')
##        case _ :
##            print('bunday baho yoq')

##def kalkulatot(a,b,amal):
##    match amal:
##        case "+":
##            return a + b
##        case "-":
##            return a - b
##        case"*":
##            return a *b
##        case "/":
##            return a /b if b != 0 else "No'lga bo'lish mumkin emas"
##        case _ :
##            return "Bunday amal mavjud emas"
##
##a = float(input("Birinchi sonni kiriting"))
##b = float(input("Ikkinchi sonni kiriting"))
##amal = input("Amalni kiriting(+ , - , * , /):  ")
##print(kalkulatot(a,b,amal))
##

def son (s):
    match s % 2:
        case 0:
            print("juft son kirittingiz")
        case 1:
            print("toq son kirittingiz")
        case _ :
            print("Butun son kiriting")
            
s = int(input("Biror bir son kiriting  : "))
print(son(s))
        



