# 多层神经网络对鸢尾花进行分类
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import tensorflow as tf

# 获取鸢尾花数据
iris = load_iris()

x_train, x_test, y_train0, y_test0 = train_test_split(iris.data, iris.target, test_size=0.25)

# 标准化处理
x_train = tf.cast(x_train-tf.reduce_mean(x_train, axis=0), tf.float32)
x_test = tf.cast(x_test-tf.reduce_mean(x_test, axis=0), tf.float32)
# 转化为独热编码
y_train = tf.one_hot(y_train0, 3)
y_test = tf.one_hot(y_test0, 3)

# 随机生成初始值(w, b)  设置隐含层包含16个神经元
w1 = tf.Variable(tf.random.normal([4, 16]))
b1 = tf.Variable(tf.zeros(16))
w2 = tf.Variable(tf.random.normal([16, 3]))
b2 = tf.Variable(tf.zeros(3))

# 学习率，迭代次数
learning_rate = 0.5
iter = 50

for i in range(iter):
    with tf.GradientTape() as tape:
        # 训练集(第一层激活函数选用relu函数， 第二层选用softmax函数-->因为目的是分类)
        y_hidden_train = tf.nn.relu(tf.matmul(x_train, w1)+b1)
        y_pre_train = tf.nn.softmax(tf.matmul(y_hidden_train, w2)+b2)
        # 交叉熵损失函数
        loss_train = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_train, y_pre_train))
    # 测试集
    y_hidden_test = tf.nn.relu(tf.matmul(x_test, w1)+b1)
    y_pre_test = tf.nn.softmax(tf.matmul(y_hidden_test, w2)+b2)
    loss_test = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_test, y_pre_test))

    # 准确率
    accuracy_train = tf.reduce_mean(tf.cast(tf.equal(tf.cast(tf.argmax(y_pre_train, axis=1), tf.float32), y_train0), tf.float32))
    accuracy_test = tf.reduce_mean(tf.cast(tf.equal(tf.cast(tf.argmax(y_pre_test, axis=1), tf.float32), y_test0), tf.float32))

    # 梯度下降
    dl_dw1, dl_db1, dl_dw2, dl_db2 = tape.gradient(loss_train, [w1, b1, w2, b2])
    w1.assign_sub(learning_rate*dl_dw1)
    b1.assign_sub(learning_rate*dl_db1)
    w2.assign_sub(learning_rate*dl_dw2)
    b2.assign_sub(learning_rate*dl_db2)

    # 训练过程结果
    print('第%d次 训练集损失函数值为%f, 识别准确率为：%f---测试集损失函数值为%f, 识别准确率为：%f' % (i+1, loss_train, accuracy_train, loss_test, accuracy_test))

print('w1的值为', w1.numpy())
print('b1的值为', b1.numpy())
print('w2的值为', w2.numpy())
print('b2的值为', b2.numpy())
