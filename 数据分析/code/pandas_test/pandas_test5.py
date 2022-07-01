# 应用：使用pandas统计出哪个小狗的名字使用得最多
import pandas as pd

# 读取csv文件
data = pd.read_csv('./code/pandas_test/dogNames2.csv')
print(data)

print('*'*40)

# 对名字使用次数进行排序
data2 = data.sort_values(by='Count_AnimalName', ascending=False)

# 打印出名字使用次数前8名
print(data2.head(8))
print('*'*40)

# pandas取行、取列
print(data2[:5])    # 取前5行
print('*'*40)

print(data2['Row_Labels'])  # 取第一列
print('*'*40)

print(data2[:5]['Row_Labels'])  # 先取行再取列
print('*'*40)

# loc[] -- 通过标签进行索引 和 iloc[] -- 通过位置进行索引

# bool索引（筛选出出现次数大于500小于1000的小狗名字）
print(data2[(data2['Count_AnimalName'] > 500) & (data2['Count_AnimalName'] < 1000)])

# 筛选出出现次数大于500的小狗名字，并且名字长度大于4
print(data2[(data2['Count_AnimalName'] > 500) & (data2['Row_Labels'].str.len() > 4)])
