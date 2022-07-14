# tensorflow对波士顿房价的预测
import tensorflow as tf
from matplotlib import pyplot as plt

# 读取数据
boston_housing = tf.keras.datasets.boston_housing
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# 归一化
x_train = (x_train-x_train.min(axis=0))/(x_train.max(axis=0)-x_train.min(axis=0))
x_test = (x_test-x_test.min(axis=0))/(x_test.max(axis=0)-x_test.min(axis=0))

# 数据处理
x0_train = tf.reshape(tf.ones(len(x_train)), (-1, 1))
x0_test = tf.reshape(tf.ones(len(x_test)), (-1, 1))
x_train = tf.concat([x0_train, x_train], axis=1)
x_test = tf.concat([x0_test, x_test], axis=1)
y_train = tf.cast(tf.reshape(y_train, (-1, 1)), dtype='float32')
y_test = tf.cast(tf.reshape(y_test, (-1, 1)), dtype='float32')

# 设置随机初始值
w = tf.Variable(tf.random.normal((14, 1)))

# 设置学习率
learning_rate = 0.01
# 迭代次数过多会出现过拟合现象
iter = 2500

mse_train = []
mse_test = []

for i in range(iter):
    with tf.GradientTape() as tape:
        # 训练集损失值
        train_pre = tf.matmul(x_train, w)
        loss_train = 0.5*tf.reduce_mean(tf.square(train_pre-y_train))
        mse_train.append(loss_train)

        # 测试集损失值
        test_pre = tf.matmul(x_test, w)
        loss_test = 0.5*tf.reduce_mean(tf.square(test_pre-y_test))
        mse_test.append(loss_test)

    print('%d、训练:%f, 测试：%f' % (i+1, loss_train, loss_test))
    dL_dw = tape.gradient(loss_train, w)
    w.assign_sub(learning_rate*dL_dw)

print('w的值为', w.numpy())

plt.figure(figsize=(16, 8), dpi=200)
plt.plot([i for i in range(2500)], mse_train, color='red')
plt.plot([i for i in range(2500)], mse_test, color='green')
plt.show()
