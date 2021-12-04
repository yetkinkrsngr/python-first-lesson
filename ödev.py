def top(x, y):
    return x+y


def cık(x, y):
    return x-y


def carp(x, y):
    return x*y


def böl(x, y):
    if y == 0:
        print("değer 0'dan küçük olamaz")
    else:
        return x/y


print(top(5, 3))
print(cık(5, 3))
print(carp(5, 3))
print(böl(6, 3))

lst = ["a", "e", "i", "o", "u"]

print(lst.count())
