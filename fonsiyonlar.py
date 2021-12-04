"Fonsiyonlar düğme gibidir basılmadan çalışmaz. def ile tanımlanır."


def button():
    print(4+1)


# aşşağıda çağırıyoruz.
button()


def button_2():
    return 2+3


s = button_2()
print(s)
# yukarıda return kullandığımızda s değişkenine değer atarız diğer türlü none , diye çevirir.

a_v = ["domates", 3, "Soğan", 2.5, "Biber", 0.5]
print(a_v)
print(a_v[0:2])

