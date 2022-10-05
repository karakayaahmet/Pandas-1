import pandas as pd
import numpy as np

m = np.random.randint(1,30,(5,3))
df1 = pd.DataFrame(m, columns=["var1","var2","var3"])

print(df1)

df2 = df1+99

print(df2)

print(pd.concat([df1,df2]))

print(pd.concat([df1,df2],ignore_index=True,axis=1))

print(df2.columns)

df2.columns = ["var1","var2","deg1"]

print(df2.columns)

print(pd.concat([df1,df2]))

print(pd.concat([df1,df2], join="inner"))

