import pandas as pd
df = pd.DataFrame([10,20,30,40],
                  columns=['numbers'],
                  index=['a','b','c','d'])
(df)
(df.index)
(df.columns)
(df.loc['c'])
df['floats'] = (1.5,2.5,3.5,4.5)
print(df)