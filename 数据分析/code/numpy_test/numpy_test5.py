# numpy数组的拼接
import numpy as np

# 设置文件路径
us_path = 'code/numpy_test/youtube_video_data/US_video_data_numbers.csv'
uk_path = 'code/numpy_test/youtube_video_data/GB_video_data_numbers.csv'

# delimiter用于指定数据之间的分隔符 dtype用于指定读取的数据类型 unpack用于对读取的数据进行转置（True）
us_data = np.loadtxt(us_path, delimiter=',', dtype='int')
uk_data = np.loadtxt(uk_path, delimiter=',', dtype='int')

# 添加一列用于区分国家
us_country = np.zeros((us_data.shape[0], 1))   # 创建一个多行一列的全0矩阵
uk_country = np.ones((uk_data.shape[0], 1))   # 创建一个多行一列的全1矩阵

# 将国家标号添加到数据的右侧(水平拼接)
us_data = np.hstack((us_data, us_country))
uk_data = np.hstack((uk_data, uk_country))

final_data = np.vstack((us_data, uk_data)).astype(int)
print(final_data)
