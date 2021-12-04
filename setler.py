s = {1, 2, 3, 4, "c"}
if "c" in s:
    print("setin icinde c harfi bulunmaktadır")
else:
    print("bulunmamaktadir.")
a = {1, 2, 3, 1, 2, 3, 3, 4, }
print(len(a))
a.add(6)
print(len(a))

s1 = {1, 3, 5, 7}
s2 = {2, 4, 5, 7}
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.intersection(s2))
print(s1.union(s2))
x = s1.union(s2)
print(s1)
print(x)
