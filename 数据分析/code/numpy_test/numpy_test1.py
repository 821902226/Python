# numpy数组的创建
import random
import numpy as np

# 方式一
arr = [1, 2, 3]
t1 = np.array(arr)
print(t1)
print(type(t1))

# 方式二
arr2 = range(5)
t2 = np.array(arr2)
print(t2)

# 方式三
t3 = np.arange(7)
print(t3)

# 指定numpy中的数据类型 (int8 可以使用 i1来代替 -- 1个字节是8位)
t4 = np.array([1, 2, 3], dtype='int8')
print(t4)
print(t4.dtype)

# 调整numpy中的数据类型
t5 = t4.astype(float)
print(t5.dtype)

# numpy保留两位小数(四舍五入)
t6 = np.array([random.random() for i in range(5)])
t7 = np.round(t6, 2)
print(t6)
print(t7)
