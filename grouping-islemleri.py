import pandas as pd
from pyparsing import col
import seaborn as sns

df = pd.DataFrame({"Gruplar":["A","B","C","A","B","C"],
                    "Veri":[10,12,35,53,69,82]}, columns=["Gruplar","Veri"])

print(df)

print(df.groupby("Gruplar"))

print(df.groupby("Gruplar").mean())

print(df.groupby("Gruplar").sum())

df2 = sns.load_dataset("planets")

print(df2.groupby("method")["orbital_period"].mean())

print(df2.groupby("method")["distance"].sum())

print(df2.groupby("method")["distance"].describe())

