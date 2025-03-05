import turtle

a = 5
def ciz(kacaKadar):
    global a
    turtle.forward(a)
    turtle.right(90)
    a += 10
    if a < kacaKadar: ciz(kacaKadar)

ciz(300)
input()