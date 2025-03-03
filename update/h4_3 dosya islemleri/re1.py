import re
metin1 = "Bugün hava çok soğuk"
metin2 = "Bursa çok sıcak"
metin3 = "Bugün hava soğuk"
metin4 = "Çok güzel bir hava var"

aranan = "çok"

print(re.search(aranan, metin4))