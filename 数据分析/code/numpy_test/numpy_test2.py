# numpy中数组的形状（几行几列）
import numpy as np

# shape是numpy数组中的一个属性 输出是一个元组 元组中数字的个数表示数组的维度
t1 = np.array([[1, 2, 3], [4, 5, 6]])
print(t1.shape)

# 修改数组的形状
t2 = t1.reshape(3, 2)
print(t2)

# 知道数组的形状，将其变成一维数组
t3 = t1.reshape(6,)
print(t3)

# 不知道数组的形状将其变成一维数组
t4 = t1.flatten()
print(t4)
