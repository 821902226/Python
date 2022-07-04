# pandas时间序列
import pandas as pd

# 生成时间
# start表示起始时间, end表示终止时间, freq表示时间间隔
print(pd.date_range(start='20210301', end='20210331', freq='D'))
print('*'*50)

# freq表示生成的时间个数
print(pd.date_range(start='20210331', periods=5, freq='M'))
print('*'*50)

# 时间间隔三天
print(pd.date_range(start='20210301', periods=5, freq='3D'))
