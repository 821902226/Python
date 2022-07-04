# scikit-learn 标准化处理
from sklearn.preprocessing import StandardScaler

data = [[1, -1, 3], [2, 4, 2], [4, 6, -1]]

standard = StandardScaler()

# 对数据进行标准化处理
data = standard.fit_transform(data)

print(data)
