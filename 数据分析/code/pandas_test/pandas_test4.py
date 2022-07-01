# pandas中DataFrame的创建
import pandas as pd
import numpy as np

# 创建DataFrame
t1 = pd.DataFrame(np.arange(15).reshape(3, 5))
print(t1)

# 设置DataFrame的index和columns
t2 = pd.DataFrame(np.arange(15).reshape(3, 5), index=list('abc'), columns=list('ABCDE'))
print(t2)
