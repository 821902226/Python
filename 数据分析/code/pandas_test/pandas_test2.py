# series的索引和切片
import pandas as pd
import string

a = {string.ascii_uppercase[i]: i for i in range(10)}

# 创建series
t1 = pd.Series(a)
print(t1)
print('*'*40)

# series的索引和切片
print(t1[3])
print('*'*40)
print(t1['B'])
print('*'*40)
print(t1[6:])
print('*'*40)
print(t1[[1, 4, 6]])
print('*'*40)
print(t1[t1 < 5])
print('*'*40)

# series中的index和values
print(t1.index)
print(t1.values)
print('*'*40)

for i in t1.index:
    print(i)

print('*'*40)

for j in t1.values:
    print(j)
