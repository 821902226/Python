# 字典特征抽取
from sklearn.feature_extraction import DictVectorizer

data = [{'city': 'Beijing', 'temp': 31}, {'city': 'Shanghai', 'temp': 28}, {'city': 'guangzhou', 'temp': 33}]

# 提取字典特征（sparse用于选择数据的显示方式）
dict = DictVectorizer(sparse=False)

# 转化后的数据
data = dict.fit_transform(data)

# 打印数据每一列对应的含义
print(dict.get_feature_names())

print(data)
