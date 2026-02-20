##def chatbot():
##    print("ZED: Salom! Men bilan gaplashing. Chiqish uchun 'exit' yozing.")
##    
##    while True:
##        user_input = input("Siz: ").lower()
##        
##        if user_input == "salom":
##            print("ZED: Salom! Qanday yordam bera olaman?")
##        elif user_input == "qanday":
##            print("ZED: Yaxshi, rahmat! Sizda yaxshimisiz?")
##        elif user_input == "isming nima?":
##            print("ZED: Mening ismim ZED!Yana qanday yordam bera olaman?")
##        elif user_input == "seni kim yaratgan?":
##            print("ZED: Meni Sobiryozov Abbosbek yaratgan.Yana qanday yordam bera olaman?")
##        elif user_input == "Stiv Jobs haqida malumot ber.":
##            print(" Steven Paul Jobs 1955-yil 24-fevralda Kaliforniya shtatidagi Mountain View shaharchasida tugʻilgan. Uning yoshlik va oʻsmirlikyillari shu yerda oʻtgan. Jobsning haqiqiy ota-onasi yosh talabalar boʻlgani va oila qurmagani uchun goʻdakni boqib olish uchun berib yuborishgan. Paul va Clara (qizlik familiyasi: Hagopian) Jobslar esa uni boqib olgan.Stevening asl otasi Abdulfattoh Jon Jandaliy (arabcha: عبد الفتاح الجندلي) — suriyalik musulmon, asl onasi Joanne Carole Schieble esa amerikalik boʻlgan Ular Universitetda tanishisgan. Ular keyinchalik oila quradi va Jandaliy siyosiy fanlar, Schieble esa tilshunoslik sohasida faoliyat yuritadi. Mona Simpson, ularning qizi va Steve Jobsning singlisi, bugun taniqli adiba. Steve Jobsning ular bilan munosabati yaxshi edi. Jobs keyinchalik opalarini qidirishga tushadi.2003-yili Steve Jobsning oshqozon osti bezida saraton paydo boʻladi. Davolanganidan keyin avvaliga oʻzini ancha yaxshi his qiladi, lekin butunlay tuzalib ketmaydi. 2009-yil jigarini transplantatsiya qildiradi. Ammo sogʻligʻi hech yaxshilanmagach 2011-yil avgust oyida Applening bosh ijrochi direktori (BID) lavozimidan bo'shaydi va boshqaruv komitetining yetakchisi qilib tayinlanadi. Steve Jobs 2011-yil 5-oktyabrda 56 yoshda undagi saratonning jadallashishi (metastazi) tufayli nafasi toʻxtab dunyodan koʻz yumdi.")
##        elif user_input == "exit":
##            print("ZED: Xayr! Yana ko‘rishguncha!")
##            break
##        else:
##            print("ZED: Kechirasiz, tushunmadim.")
##
##chatbot()


##import random
##
##javoblar = {
##    "salom": ["Salom!", "Assalomu alaykum!", "Salom, qanday yordam bera olaman?"],
##    "qanday": ["Yaxshi, rahmat! Sizda-chi?", "Zo'r! Siz-chi?", "Bugun ajoyib kun!"],
##    "isming nima?": ["Mening ismim ChatGPT!", "Men sun'iy intellekt chatbotiman.", "ChatGPT deb chaqirishingiz mumkin."],
##    "xayr": ["Xayr! Yana ko‘rishguncha!", "Salomat bo‘ling!", "Yana gaplashamiz!"]
##}
##
##def chatbot():
##    print("Chatbot: Salom! Men bilan gaplashing. Chiqish uchun 'exit' yozing.")
##    
##    while True:
##        user_input = input("Siz: ").lower()
##        
##        if user_input in javoblar:
##            print("Chatbot:", random.choice(javoblar[user_input]))
##        elif user_input == "exit":
##            print("Chatbot: Xayr!")
##            break
##        else:
##            print("Chatbot: Kechirasiz, bu haqida bilmayman.")
##
##chatbot()


def chatbot():
    print("ZED: Salom! Men bilan gaplashing. Chiqish uchun 'exit' yozing.")
    
    while True:
        user_input = input("Siz: ").lower()
        
        if user_input == "salom":
            print("ZED: Salom! Qanday yordam bera olaman?")
        elif user_input == "qanday":
            print("ZED: Yaxshi, rahmat! Sizda yaxshimisiz?")
        elif user_input == "isming nima?":
            print("ZED: Mening ismim ZED!Yana qanday yordam bera olaman?")
        elif user_input == "seni kim yaratgan?":
            print("ZED: Meni Sobiryozov Abbosbek yaratgan.Yana qanday yordam bera olaman?")
        elif user_input == "stiv jobs haqida malumot ber":
            print("Steven Paul Jobs 1955-yil 24-fevralda Kaliforniya shtatidagi Mountain View shaharchasida tugʻilgan.\n"
                  "Uning yoshlik va oʻsmirlikyillari shu yerda oʻtgan. Jobsning haqiqiy ota-onasi yosh talabalar boʻlgani\n"
                  "va oila qurmagani uchun goʻdakni boqib olish uchun berib yuborishgan. Paul va Clara (qizlik familiyasi: Hagopian) \n"
                  "Jobslar esa uni boqib olgan.Stevening asl otasi Abdulfattoh Jon Jandaliy (arabcha: عبد الفتاح الجندلي) — suriyalik \n"
                   " musulmon, asl onasi Joanne Carole Schieble esa amerikalik boʻlgan Ular Universitetda tanishisgan. Ular keyinchalik oila \n "
                   "quradi va Jandaliy siyosiy fanlar, Schieble esa tilshunoslik sohasida faoliyat yuritadi. Mona Simpson, ularning qizi va Steve \n"
                    " Jobsning singlisi, bugun taniqli adiba. Steve Jobsning ular bilan munosabati yaxshi edi. Jobs keyinchalik opalarini qidirishga\n"
                     " tushadi.2003-yili Steve Jobsning oshqozon osti bezida saraton paydo boʻladi. Davolanganidan keyin avvaliga oʻzini ancha yaxshi his qiladi, \n"
                      " lekin butunlay tuzalib ketmaydi. 2009-yil jigarini transplantatsiya qildiradi. Ammo sogʻligʻi hech yaxshilanmagach 2011-yil avgust oyida \n"
                       " Applening bosh ijrochi direktori (BID) lavozimidan bo'shaydi va boshqaruv komitetining yetakchisi qilib tayinlanadi. Steve Jobs 2011-yil \n"
                        " 5-oktyabrda 56 yoshda undagi saratonning jadallashishi (metastazi) tufayli nafasi toʻxtab dunyodan koʻz yumdi. \n Yana qanday yordam bera olaman?  ")
        elif user_input == "exit":
            print("ZED: Xayr! Yana ko‘rishguncha!")
            break
        else:
            print("ZED: Kechirasiz, tushunmadim.")

chatbot()
