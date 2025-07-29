import pandas as pd
import os

print(os.getcwd())

filePath = "Intermediate Python/CSV-Files"

var = pd.read_csv("Python/Intermediate-Python/CSV-Files/people.csv", index_col = 0)
print(var)