# 主成分分析对特征降维
from sklearn.decomposition import PCA

# 0.9表示需要保留90%的数据信息
pca = PCA(n_components=0.90)

data = pca.fit_transform([[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]])

print(data)
