import math
#girilen sayının iki fazlasının 4. kuvvetini alma31
sayi = int(input("Sayı Giriniz"))

sonuc = (sayi+2)

sonuc += math.pow(sonuc,4)
print(sonuc)