# tensorflow梯度下降法实现一元线性回归
import tensorflow as tf
import numpy as np

x = tf.constant([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
y = tf.constant([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00, 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])

learning_rate = 0.00001
iter = 100

w = tf.Variable(np.random.randn())
b = tf.Variable(np.random.randn())

for i in range(iter):
    with tf.GradientTape() as tape:
        y_pre = w*x+b
        loss = 0.5*tf.reduce_mean(tf.square(y-y_pre))
    print(i+1, loss.numpy())
    dl_dw, dl_db = tape.gradient(loss, [w, b])

    w.assign_sub(learning_rate*dl_dw)
    b.assign_sub(learning_rate*dl_db)

print('w, b的值为', w.numpy(), b.numpy())
