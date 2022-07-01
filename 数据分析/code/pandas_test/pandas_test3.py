# pandas读取外部数据
import pandas as pd

# 读取csv文件
data = pd.read_csv('./code/pandas_test/dogNames2.csv')
print(data)

# read_sql 用于读取数据库数据
# read_clipboard 用于读取剪贴板数据
# 等等
