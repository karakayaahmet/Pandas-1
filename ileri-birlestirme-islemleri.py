import pandas as pd

#birebir birleştirme
df1 = pd.DataFrame({"Çalışanlar":["Ali","Veli","Ayşe","Fatma"],
                    "Grup":["Muhasebe","Mühendislik","Mühendislik","İK"]})

print(df1)

df2 = pd.DataFrame({"Çalışanlar":["Ayşe","Ali","Veli","Fatma"],
                    "İlk Giriş":[2010,2009,2014,2019]})
print(df2)

print(pd.merge(df1,df2))

print(pd.merge(df1,df2, on="Çalışanlar"))

#çoktan teke
df3 = pd.merge(df1,df2)
print(df3)

df4 = pd.DataFrame({"Grup":["Muhasebe","Mühendislik","İK"],
                    "Müdür":["Caner","Berk","Mustafa"]})

print(df4)

print(pd.merge(df3,df4))

#many to many
df5 = pd.DataFrame({"Grup":["Muhasebe","Muhasebe","Mühendislik","Mühendislik","İK","İK"],
                    "Yetenekler":["Matematik","Excel","Kodlama","Linux","Excel","Yönetim"]})

print(df5)

print(pd.merge(df1,df5))