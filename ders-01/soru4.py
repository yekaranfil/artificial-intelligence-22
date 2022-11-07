#Pin kodu  5 defa yanlış girince bloke 5 deneme hakkı doğru giriş yapınca hoşgeldiniz


giris = 0
sayac = 0
while giris!=1563:
    giris = int(input(print("Lütfen pin kodunu giriniz")))
    sayac +=1
    if (sayac==5):
        print("pininiz bloke oldu giriş hakkı aşıldı")
        break
    else:
        if (giris == 1563):
            print("Hoş Geldiniz")
        else:
            print("Yanlış Pin")