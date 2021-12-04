x = int(input("X indexi nedir : "))
y = int(input("Y indedexi nedir: "))
print("x,y ", end="")


def endeks(x):
    for i in range(x-1):
        print("-", end="")
    print(x, end="")
    for a in range(x-1):
        print("-", end="")


def index(y):
    for q in range(y-1):
        print("|")
    print(y, end="")
    print(" "*x, "*")
    for w in range(y-1):
        print("|")


endeks(x)
index(y)
