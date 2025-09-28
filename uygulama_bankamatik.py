# Bankamatik uygulaması

# Hesap bilgileri tutulacak (dict)
# menu , paraCekme , bakiyeSorgulama , paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
{
    "isim" : "Gökçe Sarıçam",
    "hesapNo" : "12345", #str
    "bakiye" : 20000, #int
    "ekHesap" : 5000,
    "username" : "gokcesaricam",
    "password" : "1234",
    "ekHesapLimit" : 10000
}
# {
#     "isim" : "Ekin Koçyiğit",
#     "hesapNo" : "12345", #str
#     "bakiye" : 30000, #int
#     "ekHesap" : 10000,
#     "username" : "ekinkocyigit",
#     "password" : "1234",
#     "ekHesapLimit" : 15000
# }
]

def kayitOl():
    print("\n=== KAYIT OL ===")
    isim = input("Adınız ve Soyadınız: ")
    username = input("Kullanıcı adı: ")

    # Kullanıcı adı kontrolü (Zaten kayıtlı mı?)
    for hesap in hesaplar:
        if hesap["username"] == username:
            print("Bu kullanıcı adı zaten alınmış! Lütfen başka bir isim deneyin.")
            return kayitOl()

    password = input("Şifre: ")
    hesapNo = str(len(hesaplar) + 10000)  # Otomatik hesap numarası
    bakiye = float(input("Başlangıç bakiyenizi giriniz: "))
    ekHesapLimit = float(input("Ek hesap limitinizi giriniz: "))

    yeni_hesap = {
        "isim": isim,
        "hesapNo": hesapNo,
        "bakiye": bakiye,
        "ekHesap": ekHesapLimit,
        "username": username,
        "password": password,
        "ekHesapLimit": ekHesapLimit
    }

    hesaplar.append(yeni_hesap)
    print("\n Kayıt tamamlandı! Şimdi giriş yapabilirsiniz.")

def menu(hesap):
    while True:
        print("\n=== ANA MENÜ ===")
        print(f"Merhaba,{hesap["isim"]}!")
        print("1 : Bakiye Sorgulama")
        print("2 : Para Çekme")
        print("3 : Para Yatırma")
        print("4 : Çıkış")

        islem = input("Yapmak istediğiniz işlem(1-4): ")

        if islem == "1":
            bakiyeSorgulama(hesap)
        elif islem == "2":
            paraCekme(hesap)
        elif islem == "3":
            paraYatirma(hesap)
        elif islem == "4":
            print("Çıkış yapılıyor...")
            break    
        else:
            print("Hatalı bir tuşlama yaptınız.(1-4)")
        if not devamMi():
            print("Çıkış yapılıyor...")
            break

def devamMi():
    while True:
        secim = input("\nAna menüye dönmek ister misiniz? (E/H): ").strip().upper()
        if secim == "E":
            return True
        elif secim == "H":
            return False
        else:
            print("Geçersiz giriş! Lütfen 'E' veya 'H' giriniz.")

def paraYatirma(hesap):
    tutar = float(input("Yatırmak istediğiniz tutarı giriniz: "))

    hesap["bakiye"] += tutar
    print(f"Para yatırma işlemi başarılı. Yeni bakiyeniz: {hesap['bakiye']} TL")

def bakiyeSorgulama(hesap):
    print(f"Bakiye bilgisi: {hesap["bakiye"]} TL")
    print(f"Ek bakiye: {hesap["ekHesap"]} TL")

def paraCekme(hesap):
    miktar = float(input("Çekmek istediğiniz miktar: "))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekHesapKullanimIzni = input("Ek hesap kullanılsın mı? (E/H): ").strip().upper()
            if ekHesapKullanimIzni == "E":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            elif ekHesapKullanimIzni == "H":
                print("İzin verilmedi,bakiye yetersiz")
            else:
                print("Yanlış ya da eksik bir tuşlama yaptınız.")
        else:
            print("Bakiye yetersiz.")


def login():
     while True:
        print("\n=== GİRİŞ EKRANI ===")
        print("1: Giriş Yap")
        print("2: Kayıt Ol")
        print("3: Çıkış")

        secim = input("Seçiminizi yapınız (1-3): ")

        if secim == "1":
            username = input("Kullanıcı Adı: ")
            password = input("parola: ")


            for hesap in  hesaplar:
                if hesap["username"] == username and hesap["password"] == password:
                    print("Giriş başarılı!")
                    menu(hesap)
                    return
            
            print("Hatalı kullanıcı adı veya parola! Tekrar deneyin.")
        elif secim == "2":
            kayitOl()

        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz giriş! Lütfen 1-3 arasında bir seçim yapın.")


login()



