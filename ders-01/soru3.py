sayi1 = 1
sayac = 0
toplam = 0
while sayi1>0:
    sayi1 = int(input("Bir sayı Giriniz"))
    toplam += sayi1
    sayac+=1
    print(toplam)
    if(sayi1 == 0):
        ortalama = float(toplam/sayac)
        print("Ortalama :",ortalama)