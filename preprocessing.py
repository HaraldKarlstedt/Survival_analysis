import pandas as pd
import numpy as np

data = pd.read_csv("lung_cancer.csv")


#Create data set with only odd rows 
data_odd_rows = data.iloc[::2]
data_even_rows = data.iloc[1::2]

data_out = data_odd_rows.copy()
data_out[["TIME", "Y"]] = data_even_rows[["TIME", "Y"]].to_numpy() - data_odd_rows[["TIME", "Y"]].to_numpy()

data_out.to_csv("reformated_data.csv", index = False)