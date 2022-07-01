# 使用numpy读取数据绘制直方图
import numpy as np
from matplotlib import pyplot as plt

us_path = 'code/numpy_test/youtube_video_data/US_video_data_numbers.csv'
us_data = np.loadtxt(us_path, delimiter=',', dtype='int')
us_data = us_data[:, 3]
us_data = us_data[us_data <= 5000]

interval = 500
group_count = (max(us_data)-min(us_data))//interval

plt.figure(figsize=(16, 8), dpi=100)

x = list(range(11))
x = [i*500 for i in x]
plt.xticks(x)

# 可以使用列表来对分组进行指定， 避免直接设置分组数出现的问题
plt.hist(us_data, x)
plt.show()
