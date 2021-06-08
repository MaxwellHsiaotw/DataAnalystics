import pandas as pd
elc = pd.read_csv("elc.csv")
a = elc.isnull().sum()
v = elc.columns
print(v)
for i in range(0,4):
	print(v[i])