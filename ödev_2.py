liste = list()
giriş = """
[H]=========HARMAN========[-][o][x]
|                                 |
|     Programa Hoşgeldiniz!       |
|           Sürüm 0.1             |
|    yapılakcak işlemi seçiniz.   |
|           1- Ekle.              |
|           2- Sil.               |
|           3- Güncelle.          |
|           4- Liste görüntüle.   |
|           2- Çıkış.             |
|=================================|

"""
print(giriş)
h = 1
while h == 1:
    x = int(input("hangi işlemi yapmak istersiniz : "))
    if x == 1:
        gir = input("deger : ")
        liste.append(gir)
        print(liste)
        x = 0
    elif x == 2:
        print("hangi degeri silmek istersiniz index degerini giriniz: ")
        sil = int(input("silinecek değer : "))
        liste.pop(sil)
        x = 0
    elif x == 3:
        print("hangi elemanı güncellemek istersiniz : ")
        print(liste)
        nr = input("Yerine yazıcak olan eleman : ")
        nn = int(input("index no : "))
        liste.insert(nn, nr)
        y = int(input("silinecek olan eleman : "))
        y += 1
        del liste[y]
        x = 0
    elif x == 4:
        print(liste)
        x = 0
    elif x == 5:
        x == 0
        h == 0
        print("yeniden bekleriz....")
        break
