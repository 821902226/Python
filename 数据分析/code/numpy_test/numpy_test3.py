# numpy读取本地数据
import numpy as np

# 设置文件路径
data_path = 'code/numpy_test/youtube_video_data/US_video_data_numbers.csv'

# delimiter用于指定数据之间的分隔符 dtype用于指定读取的数据类型 unpack用于对读取的数据进行转置（True）
t1 = np.loadtxt(data_path, delimiter=',', dtype='int32', unpack=True)

print(t1)

# numpy中的数组转置
t2 = np.array([[1, 2, 3], [4, 5, 6]])

# 方法一
t3 = t2.transpose()
print(t3)

# 方法二
t4 = t2.T
print(t4)
