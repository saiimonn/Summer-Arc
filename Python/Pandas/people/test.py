import pandas as pd
import os

print(os.getcwd())

var = pd.read_csv("CSV-Files/people.csv", index_col = 0)
print(var)