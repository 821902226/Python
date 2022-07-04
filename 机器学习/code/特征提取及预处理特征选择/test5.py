# scikit-learn 归一化处理
from sklearn.preprocessing import MinMaxScaler

data = [[23, 41, 36], [30, 5, 9]]

# feature_range指定数据归一化的范围, 默认为（0, 1）
mm = MinMaxScaler(feature_range=(0, 10))

# 对数据进行归一化
data = mm.fit_transform(data)

print(data)
