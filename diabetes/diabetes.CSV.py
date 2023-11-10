import numpy as np
import pandas as pd
data = pd.read_excel(r"C:\Users\LUCY\Documents\Lucy Gachogu Documents\HR Files\Coding Baby-Steps\Exercises Files\Backpropagation\backpropagation\diabetes.xlsx")
df = pd.DataFrame(data, columns=["weight"])

print(df)