import pandas as pd

df = pd.DataFrame({"Gruplar":["A","B","C","A","B","C"],
                    "degisken1":[23,34,52,123,51,25],
                    "degisken2":[123,234,523,532,512,345]},columns=["Gruplar","degisken1","degisken2"])

print(df)

print(df.groupby("Gruplar").aggregate(["min","max","median"]))

print(df.groupby("Gruplar").aggregate({"degisken1":max, "degisken2":min}))