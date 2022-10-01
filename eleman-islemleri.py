import numpy as np
import pandas as pd

a = np.array([1,2,3,4,5])
b = pd.Series(a)

print(b)

print(b[0])

print(b[0:3])

seri = pd.Series([1,2,3,4,5], index=["A","B","C","D","E"])

print(seri.index)

print(seri.keys)

print(seri.values)

print(seri.items())

# eleman sorgulama

"a" in seri

print("a" in seri)

print("A" in seri)

