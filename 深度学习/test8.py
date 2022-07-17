# tensorflow对鸢尾花分类(多分类)
from sklearn.datasets import load_iris
import tensorflow as tf

# 获取鸢尾花数据
iris = load_iris()

# 从三种花中取出两个品种
x_train = iris.data
y_train = iris.target

# 数据处理
x0_train = tf.ones([len(x_train), 1])
x_train = (x_train-x_train.min(axis=0))/(x_train.max(axis=0)-x_train.min(axis=0))
x_train = tf.concat([x0_train, x_train], axis=1)
# 转化为独热编码
y_train = tf.one_hot(y_train, 3)


# 随机生成初始值(w, b)
w = tf.Variable(tf.random.normal([5, 3]))

# 学习率，迭代次数
learning_rate = 0.15
iter = 500

# 训练模型
for i in range(iter):
    with tf.GradientTape() as tape:
        y_pre = tf.nn.softmax(tf.matmul(x_train, w))
        loss = -tf.reduce_sum(y_train*tf.math.log(y_pre))
    # 计算预测的准确率
    accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.cast(tf.argmax(y_pre, axis=1), tf.float32), iris.target), tf.float32))

    # 梯度下降法更新w的值
    dl_dw = tape.gradient(loss, w)
    w.assign_sub(learning_rate*dl_dw)

    print('第%d次 损失函数值为%f, 识别准确率为：%f' % (i+1, loss, accuracy))
print('w的值为', w.numpy())
