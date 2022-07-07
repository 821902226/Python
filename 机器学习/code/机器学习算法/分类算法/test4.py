# 决策数预测泰坦尼克号人员是否生存
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split


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

dec = DecisionTreeClassifier(criterion='gini', max_depth=6)

dec.fit(x_train, y_train)

score = dec.score(x_test, y_test)

print('准确率：', score)
