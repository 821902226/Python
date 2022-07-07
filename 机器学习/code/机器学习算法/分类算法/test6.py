# 随机森林预测泰坦尼克号人员是否生存
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV

path = '~/Machine learning data/泰坦尼克号幸存者数据/train.csv'

# 读取数据
data = pd.read_csv(path)

x = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
y = data['Survived']

# 将年龄缺失值补充为平均值
x['Age'].fillna(x['Age'].mean(), inplace=True)

dict = DictVectorizer(sparse=False)
x = dict.fit_transform(x.to_dict(orient='records'))

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.25)

rf = RandomForestClassifier()

param = {'n_estimators': [100, 300, 500, 800, 1000], 'max_depth': [5, 8, 15, 20, 24]}

gc = GridSearchCV(rf, param_grid=param, cv=5)

gc.fit(x_train, y_train)

print('预测的准确率：', gc.score(x_test, y_test))

print('选择最好的参数：', gc.best_params_)
