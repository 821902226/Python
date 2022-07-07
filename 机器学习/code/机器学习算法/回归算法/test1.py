# 线性回归算法预测房价
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.metrics import mean_squared_error

lb = load_boston()

# 应该先分割数据集，然后进行标准化
x = lb.data
y = lb.target
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.25)

# 特征值和目标值都需要标准化
ss_x = StandardScaler()
x_train = ss_x.fit_transform(x_train)
x_test = ss_x.transform(x_test)
ss_y = StandardScaler()
y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
y_test = ss_y.transform(y_test.reshape(-1, 1))

# 1.正规方程方式求解预测结果
lr = LinearRegression()
lr.fit(x_train, y_train)

# 求出的w系数
# print(lr.coef_)

y_predict = lr.predict(x_test)
y_predict = ss_y.inverse_transform(y_predict)
print('方式一的均方误差： ', mean_squared_error(y_predict, ss_y.inverse_transform(y_test)))
# print('预测的房价是：', y_predict.astype('int').flatten())

# 2.梯度下降方式求解预测结果
sgd = SGDRegressor()
sgd.fit(x_train, y_train)
# 求出的w系数
# print(sgd.coef_)

y_predict = sgd.predict(x_test)
y_predict = ss_y.inverse_transform(y_predict.reshape(-1, 1))
print('方式二的均方误差： ', mean_squared_error(y_predict, ss_y.inverse_transform(y_test)))
# print('预测的房价是：', y_predict.astype('float').flatten())

# 3.岭回归求解预测结果（降低高次项的系数，减小过拟合）
ridge = Ridge(alpha=1.0)
ridge.fit(x_train, y_train)

y_predict = ridge.predict(x_test)
y_predict = ss_y.inverse_transform(y_predict.reshape(-1, 1))
print('方式三的均方误差： ', mean_squared_error(y_predict, ss_y.inverse_transform(y_test)))
