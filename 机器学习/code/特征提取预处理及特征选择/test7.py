# 特征选择--过滤式(将方差小的特征删除)
from sklearn.feature_selection import VarianceThreshold

# 0.0表示将所有相同的特征删除(threshold指定方差的大小)
variance = VarianceThreshold(threshold=0.0)

data = variance.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

print(data)
