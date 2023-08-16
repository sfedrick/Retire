

from interest import *
import pandas as pd
# inflation = pd.read_csv("inflation.csv")
# print(inflation.loc[0,'year'])

savings = Assets(0,25,120000,0,inflation=1,returns=1,four01k=0)
promotions = pd.read_csv("test.csv")
savings.promotion_extraction(promotions)
print(savings.compound_interest())

