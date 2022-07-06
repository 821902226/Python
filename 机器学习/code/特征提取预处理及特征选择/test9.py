# 数据集与数据的划分
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 获取鸢尾花数据集
iris = load_iris()

print(iris.data)            # 特征数据
print(iris.target)          # 标签数组
print(iris.feature_names)   # 特征名称
print(iris.target_names)    # 标签名称

print('*' * 50)

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25)

print("训练集： \n", x_train, y_train)
print('*' * 50)
print("测试集： \n", x_test, y_test)
