# bir kere çevirdiğimizde kendi kendine dönüyor.
# recorself öz yenineleme bu biraz daha
def bisiklet(x):
    if x > 0:
        x-1
        print("Pedal Döndü")
        return bisiklet(x)
    else:
        print("pedal durdu !!!")
        return 1

# asal sayı bulma


def asal(x):
    deger = 0
    for i in range(1, x+1):
        if x % i == 0:
            deger = deger + 1
    if deger < 3:
        print(x, end=",")
    if x > 2:
        x = x - 1
        return asal(x)


asal(30)


def hello(x):
    if x > 0:
        print("Merhaba Dünya")
        x -= 1
        return hello(x)
    elif x == 0:
        print("done")
        pass


hello(10)
