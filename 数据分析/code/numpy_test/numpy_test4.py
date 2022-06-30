# numpy索引和切片

import numpy as np

# 设置文件路径
data_path = 'code/numpy_test/youtube_video_data/US_video_data_numbers.csv'

# delimiter用于指定数据之间的分隔符 dtype用于指定读取的数据类型 unpack用于对读取的数据进行转置（True）
t1 = np.loadtxt(data_path, delimiter=',', dtype='int32')
print(t1)
print('*'*50)

# 取一行
print(t1[1])
print('*'*50)

# 取连续的多行
print(t1[1:4])
print('*'*50)

# 取不连续的多行
print(t1[[1, 3, 5]])
print('*'*50)

# 取一列（逗号左边代表行，逗号右边代表列）
print(t1[:, 1])
print('*'*50)

# 取不连续的多列
print(t1[:, [1, 3]])

# 取第三行第二列的值
print(t1[2, 1])

# 根据条件赋值
t2 = np.arange(12).reshape(3, 4)
print(t2)

t2[t2 < 6] = 6
print(t2)

# numpy中的三元运算符
t3 = np.where(t2 == 6, 8, 3)
print(t3)

# 裁剪（小于8的替换为8, 小于10的替换为10）
t4 = t2.clip(8, 10)
print(t4)
