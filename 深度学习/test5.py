# tensorflow梯度下降法实现多元线性回归
import tensorflow as tf
import numpy as np

area = tf.constant([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
room = tf.constant([3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 1, 1, 1, 2, 2], dtype='float32')
price = tf.constant([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00, 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])

learning_rate = 0.1
iter = 100

# w0就是b
w = tf.Variable(tf.random.normal([3, 1]))

# 归一化
x0 = tf.ones(len(area))
x1 = (area-min(area))/(max(area)-min(area))
x2 = (room-min(room))/(max(room)-min(room))
x = np.stack((x0, x1, x2), axis=1)
y = price.numpy().reshape(-1, 1)

for i in range(iter):
    with tf.GradientTape() as tape:
        # 矩阵相乘
        y_pre = tf.matmul(x, w)
        # 求损失函数
        loss = 0.5*tf.reduce_mean(tf.square(y-y_pre))
    print(i+1, loss.numpy())
    # 求偏导
    dl_dw = tape.gradient(loss, w)
    # 梯度下降
    w.assign_sub(learning_rate*dl_dw)

print('w的值为', w.numpy())
