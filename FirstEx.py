import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Ex = pd.ExcelFile(r"SAEA08_FING-raw-PM_10740-2017_01_19-03_01_53__232.xlsx")
Data1 = pd.read_excel(r"SAEA08_FING-raw-PM_10740-2017_01_19-03_01_53__232.xlsx",sheetname=0)

read_sheet_name = Ex.sheet_names

print (read_sheet_name)
print (Data1.iloc[1:,[0,3]])

#pvt = Data1.pivot_table(values = ["SAE-GW session act SR"], columns = "FING name", index="Period start time", aggfunc="max")
#print (pvt)

Data2 = Data1.iloc[1:,[0,3]]
#Data2 = Data2.cumsum()
