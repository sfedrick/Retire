from interest import *
import pandas as pd
# inflation = pd.read_csv("inflation.csv")
# print(inflation.loc[0,'year'])

savings = Assets(0,25,120000,12000)
savings.compound_interest()