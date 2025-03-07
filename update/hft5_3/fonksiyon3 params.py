def topla (*sayilar):
    print(sayilar)
    print(type(sayilar))
    toplam = 0
    for a in sayilar:
        toplam += a
    print("Toplam:",toplam)

toplanacaklar = [2,5,3,8]

topla(*toplanacaklar)
topla(2,5,3,8)
topla(2,5,3,8)