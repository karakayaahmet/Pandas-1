import numpy as np
import pandas as pd

m = np.random.randint(0,30,(10,3))

df = pd.DataFrame(m, columns=["var1", "var2", "var3"])

print(df)

print(df["var1"])

print(df["var1"][0:3])

print(df[0:3][["var1","var2"]])  #fancy ile yap

print(df[df.var1>10]["var2"])

print(df[(df["var1"] > 10) & (df["var3"] < 5)])

print(df[(df.var1 > 10) & (df.var3 < 8)])