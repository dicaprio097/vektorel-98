print("Bölme işlemi")

try:
    a = input("Bölünecek sayı nedir?")
    b = input("Bölen sayı nedir?")
    a = int(a)
    b = int(b)
    print(a / b)

except ValueError:
    print("Yanlış değer girişi!")

except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")

except Exception as hata:
    print("Bir hata oluştu:", hata)

else: pass

finally:
    print("İşlem bitti.")