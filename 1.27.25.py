# class Talaba :
#     def __init__(self,ism,familya,tyil):
#         self.ism = ism
#         self.failya = familya
#         self.tyil = 2010
#         self.bosqich = 1
        
#     def tanishtir (self):
#       return  f"Menisng ismim {self.ism}, familyam {self.failya} , yoshim { 2025 - self.tyil} va men {self.bosqich} - bosqichtaman"




# Talaba1 = Talaba("Asad" , "Komilv", 2010)
# Talaba2 = Talaba("murot" , "Komilv", 2015)

# class Kitob:
#     def __init__(self,nomi,muallifi,nyil):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.nyil = nyil
#         self.sahifa = 227
#         self.narh = 57000


#     def malumot(self):
  

#       return f'Kitob {self.nomi}, muallifi {self.muallifi} {self.nyil}- yilda nashr qilingan, kitob {self.sahifa} sahifali narxi:{self.narh} som '

# kitob1 = Kitob("men va pul", "Saidmurod Davlatov", 2022 )
class Komptr:
    def __init__(self,model,narx):
        self.model = model
        self.narx = narx
       # self.prosesor = core
        self.xotira = 526 

    def malumot (self):
        return  f"{self.model} modelli kompyuter narxi {self.narx} dollor$   va xotirasi {self.xotira}"

komptr1 = Komptr("HP", 500)
komptr2 = Komptr("Lenovo", 300)
komptr3 = Komptr("mackbook", 1000)