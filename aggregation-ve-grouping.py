#basit toplulaştırma yöntemleri
#count()
#first()
#last()
#mean()
#median()
#min()
#max()
#std()
#var()
#sum()

import seaborn as sns

df = sns.load_dataset("planets")
print(df.head())

print(df.shape)

print(df.mean())

print(df["mass"].mean())

print(df["mass"].count())

print(df["mass"].min())

print(df["mass"].max())

print(df["mass"].sum())

print(df.describe())

print(df.describe().T)

print(df.info())