import qrcode
import time

Oluşturulacak_Metin = input("Oluşturulacak Metini Giriniz('q' ile durdurabilirsiniz):")

path = "C:/Users\Ömer\Desktop/qrcode.png"

while True:

    if Oluşturulacak_Metin.lower() == "q":
        print("Qr Kod Oluşturma Durduruldu")
        time.sleep(3)
        break
    else:
        print("Program Çalışmaya Başladı Lütfen Bekleyiniz")
    try:
        img = qrcode.make(Oluşturulacak_Metin)
        img.save(path)
        print("İçerik Kaydedildi")
    finally:
        print("Program Sonlandırıldı")
        time.sleep(3)
        break

print("This program is created omertopal")
print("Thank you for using.")