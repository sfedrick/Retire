

from interest import *
import pandas as pd
# inflation = pd.read_csv("inflation.csv")
# print(inflation.loc[0,'year'])

savings = Assets(0,25,0,0)
debt = pd.read_csv("test.csv")
savings.debt_horizon(debt)
print(savings.compound_interest())