import pandas as pd
import numpy as np

l = [1,2,3,4,5]

sonuc =pd.DataFrame(l,columns=["degişken değerleri"])

print(sonuc)

m = np.arange(1,10).reshape(3,3)

print(pd.DataFrame(m,columns=["var1","var2","var3"]))

# dataframe isimlendirme

df = pd.DataFrame(m, columns=["var1", "var2", "var3"])

df.columns = ("deg1", "deg2", "deg3")

print(df)

print(type(df))

print(df.axes)

print(df.ndim)

print(df.shape)

print(df.size)

print(df.values)

a = np.array([1,2,3,4,5])

df1 = pd.DataFrame(a, columns=["deg"])

print(df1)