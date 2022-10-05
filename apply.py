import pandas as pd
import numpy as np

df = pd.DataFrame({"Gruplar":["A","B","C","A","B","C"],
                    "degisken1":[1,34,53,52,34,55],
                    "degisken2":[34,543,342,5,335,534]},
                    columns=["Gruplar","degisken1","degisken2"])

print(df)

print(df.apply(np.sum))

print(df.groupby("Gruplar").apply(np.mean))

print(df.groupby("Gruplar").apply(np.sum))