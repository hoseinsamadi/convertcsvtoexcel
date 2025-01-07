from os import write
import pandas as pd
df = pd.read_csv('test_csv.csv')
df.to_excel('test.xlsx',index=False)


