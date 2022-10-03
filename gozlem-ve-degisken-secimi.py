import numpy as np
import pandas as pd

m = np.random.randint(0,30,(10,3))
df = pd.DataFrame(m, columns=["var 1", "var 2", "var 3"])

print(df)

#loc: tanımlandığı şekliyle seçim yapmak için kullanılır.
#iloc: alışık olduğumuz indexleme mantığı ile seçim yapar.

print(df.loc[0:3])

print(df.iloc[0:3])

print(df.loc[0:3,"var 3"])