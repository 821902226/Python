# tensorflow实现逻辑回归算法对鸢尾花分类（二分类）
from sklearn.datasets import load_iris
import tensorflow as tf

# 获取鸢尾花数据
iris = load_iris()

# 从三种花中取出两个品种
x_train = iris.data[:100]
y_train = iris.target[:100]

# 数据处理
x0_train = tf.ones([len(x_train), 1])
x_train = (x_train-x_train.min(axis=0))/(x_train.max(axis=0)-x_train.min(axis=0))
x_train = tf.concat([x0_train, x_train], axis=1)
y_train = tf.cast(tf.reshape(y_train, [-1, 1]), 'float32')

# 随机生成初始值(w, b)
w = tf.Variable(tf.random.normal([5, 1]))

# 学习率， 迭代次数
learning_rate = 0.04
iter = 200

for i in range(iter):
    with tf.GradientTape() as tape:
        # sigmoid函数
        y_pre = 1/(1+tf.exp(-tf.matmul(x_train, w)))
        # 计算对应的损失值
        loss = -tf.reduce_mean(y_train*tf.math.log(y_pre)+(1-y_train)*tf.math.log(1-y_pre))

    # 计算预测的准确率
    y_pre = tf.where(y_pre < 0.5, 0.0, 1.0)
    # 转化为float类型， 避免小数部分被去掉（平均值就是对应的准确率）
    accuracy = tf.reduce_mean(tf.cast(tf.equal(y_pre, y_train), tf.float32))

    # 梯度下降法更新w的值
    dl_dw = tape.gradient(loss, w)
    w.assign_sub(learning_rate*dl_dw)

    print('第%d次 损失函数值为%f, 识别准确率为：%f' % (i+1, loss, accuracy))
print('w的值为', w.numpy())
