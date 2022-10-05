import pandas as pd

df = pd.DataFrame({"Gruplar":["A","B","C","A","B","C"],
                    "degisken1":[11,34,23,45,54,23],
                    "degisken2":[234,123,252,542,534,134]}, columns=["Gruplar","degisken1","degisken2"])

print(df)

def filter_func(x):
    return x["degisken1"].std()>9

print(df.groupby("Gruplar").std())

print(df.groupby("Gruplar").filter(filter_func))