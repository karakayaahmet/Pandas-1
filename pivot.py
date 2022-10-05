from operator import index
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.head())

print(titanic.groupby("sex")["survived"].mean())

print(titanic.groupby(["sex","class"])["survived"].aggregate("mean").unstack())

#pivot ile table
print(titanic.pivot_table("survived",index="sex",columns="class"))

age = pd.cut(titanic["age"],[0,18,90])

print(age.head())

print(titanic.pivot_table("survived", index=["sex",age], columns="class"))