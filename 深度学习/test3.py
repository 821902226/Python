# 一元线性回归预测房价(解析法)
import tensorflow as tf

x_train = tf.constant([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
y_train = tf.constant([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00, 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])

x_mean = tf.reduce_mean(x_train)
y_mean = tf.reduce_mean(y_train)

xy_sum = tf.reduce_sum((x_train-x_mean)*(y_train-y_mean))
x_sum = tf.reduce_sum((x_train-x_mean)*(x_train-x_mean))

w = xy_sum/x_sum
b = y_mean-w*x_mean

# 训练结果
print('w:', w.numpy())
print('b:', b.numpy())

# 进行预测
x = tf.constant(112.00)

y_predict = w * x + b
print('房子的价格是：', y_predict.numpy())
