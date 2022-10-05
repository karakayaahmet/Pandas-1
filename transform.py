import pandas as pd

df = pd.DataFrame({"Gruplar":["A","B","C","A","B","C"],
                    "degisken1":[1,34,53,55,34,42],
                    "degisken2":[23,542,355,342,523,135]}, 
                    columns=["Gruplar","degisken1","degisken2"])

print(df)

print(df["degisken1"]*9)

df_a = df.iloc[:,1:3]

print(df_a.transform(lambda x: x-x.mean()))