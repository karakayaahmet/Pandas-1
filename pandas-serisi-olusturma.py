import pandas as pd

pd.Series([1,2,3,4,5])

seri = pd.Series([1,2,3,4,5])

print(type(seri))

print(seri.axes)

print(seri.dtype)

print(seri.size)

print(seri.ndim)

print(seri.values)

seri.head()

print(seri.head(3))

print(seri.tail(3))

# index isimlendirmesi

p = pd.Series([1,3,4,2,5], index=[1,3,5,7,9])

print(p)

s = pd.Series([1,2,3,4,5], index = ["a","b","c","d","e"])

print(s)

print(s["a":"c"])

# sözlük üzerinden liste oluşturmak

sozluk = pd.Series({"reg":10, "loj":20, "cart":30})

print(sozluk)

soz = {"Elazığ":23, "Malatya":44, "Diyarbakır":21}

yeni_soz = pd.Series(soz)

print(yeni_soz)

# iki seriyi birleştirerek seri oluşturma

print(pd.concat([sozluk,yeni_soz]))