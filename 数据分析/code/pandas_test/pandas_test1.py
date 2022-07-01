# pandas创建Series
import pandas as pd

# Series相当于带标签的数组
# 方式一 通过列表创建Series
t1 = pd.Series([1, 2, 3, 4])
print(t1)

# 创建Series指定标签
t2 = pd.Series([1, 2, 3, 4], index=list('abcd'))
print(t2)

# 方式二 通过字典创建Series
dict1 = {'id': '8219', 'name': 'xiaoming', 'gender': 'man'}
t3 = pd.Series(dict1)
print(t3)

# Series数据类型的修改与numpy一样
print(t1.dtype)
t4 = t1.astype(float)
print(t4.dtype)
