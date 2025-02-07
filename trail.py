import numpy as np
import pandas as pd

df = pd.DataFrame({'x': [92, 56, 88, 70, 80, 49, 65, 35, 66, 67], 
                   'y': [98, 68, 81, 80, 83, 52, 66, 30, 68, 73]})

corelation =  df['x'].corr(df['y'])
print(corelation)