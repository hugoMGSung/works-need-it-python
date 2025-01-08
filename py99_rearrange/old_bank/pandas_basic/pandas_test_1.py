import pandas as pd
import numpy as np

data = list(range(101, 106))
series1 = pd.Series(data, dtype='float')
print(f'series1 =>\n{series1}')

arr1 = np.array(data)
series2 = pd.Series(arr1)
print(f'series2 =>\n{series2}')

arr2 = np.arange(101, 106)
series3 = pd.Series(arr2, dtype='int64')
print(f'series3 =>\n{series3}')