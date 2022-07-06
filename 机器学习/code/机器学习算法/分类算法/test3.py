# 交叉验证与网格搜索找到K-近邻算法的最佳参数
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

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

# 进行网格搜索
knn = KNeighborsClassifier()
param = {"n_neighbors": [i for i in range(8, 10, 14)]}
# knn指定算法，param_grid指定需要测试的参数，cv指定交叉验证的次数
gc = GridSearchCV(knn, param_grid=param, cv=2)

gc.fit(x_train, y_train)

# 预测的准确率
print('预测的准确率：', gc.score(x_test, y_test))

print('交叉验证最好的结果：', gc.best_score_)

print('选择最好的模型：', gc.best_estimator_)

print('选择最好的参数：', gc.best_params_)

print('每次交叉验证的结果：', gc.cv_results_)
