# 逻辑回归进行乳腺癌预测（根据细胞特征）
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

path = '~/Machine learning data/癌症预测数据/breast-cancer-wisconsin.data'

column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']

data = pd.read_csv(path, names=column)

# 处理缺失值
data = data.replace(to_replace='?', value=np.nan)
data = data.dropna()

x = data[column[1:10]]
y = data[column[10]]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2)

# 标准化
ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

lr = LogisticRegression(C=1.0)

lr.fit(x_train, y_train)
y_predict = lr.predict(x_test)

# 得到的方程系数
print('方程系数', lr.coef_)
# 预测的准确率
print('预测的准确率', lr.score(x_test, y_test))

print('召回率', classification_report(y_test, y_predict, labels=[2, 4], target_names=['良性', '恶性']))
