import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,44,1])

print(s)


dates = pd.date_range('20160101',periods=10)
df = pd.DataFrame(np.random.randn(10,4),index=dates,columns=['a','b','c','d'])

print(df)

print("00000000000000000000000000000000000")
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)
print("------------------------------------")
print(df2.values)
print("==========================")
print(df2.describe())