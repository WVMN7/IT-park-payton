s = input("Biror bir matn kirit:  ")
katta_harf = "".join([char for char in s if char.isupper()])
print("Katta harflar:" , katta_harf)