# K-近邻算法预测用户入住酒店位置
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

path = '~/Downloads/train.csv'

# 读取训练数据
data = pd.read_csv(path)
# 缩小范围，减小运算时间
data = data.query('x > 1.00 & x < 1.25 & y > 1.50 & y < 1.75')

# 对时间进行转化
time = pd.to_datetime(data['time'], unit='s')
time = pd.DatetimeIndex(time)
data.loc[:, 'hour'] = time.hour
data.loc[:, 'weekday'] = time.weekday
data = data.drop(['time'], axis=1)

# 将入住人数较少的酒店删除
place_count = data.groupby('place_id').count()
tf = place_count[place_count.row_id > 3].reset_index()
data = data[data['place_id'].isin(tf.place_id)]

# 取出数据中的特征值和目标值
x = data.drop(['place_id', 'row_id'], axis=1)
y = data['place_id']

# 对数据集进行分割(训练集和测试集)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# 特征工程（特征值标准化）
standard = StandardScaler()
x_train = standard.fit_transform(x_train)
x_test = standard.transform(x_test)

# 利用数据集进行训练
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train, y_train)

# 预测结果
y_predict = knn.predict(x_test)
print('预测用户的入住位置是：\n', y_predict)

# 预测的准确率
score = knn.score(x_test, y_test)
print('预测的准确率是：', score)
