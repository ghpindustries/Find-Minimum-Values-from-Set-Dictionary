import pandas as pd

adict ={'a':2,'b':4,'c':6,'d':8,'e':10}

series = pd.Series(adict)
print((series).min())
