# 单层神经网络对鸢尾花进行分类
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

# 随机生成初始值(w, b)
w = tf.Variable(tf.random.normal([4, 3]))
b = tf.Variable(tf.zeros(3))

# 学习率，迭代次数
learning_rate = 0.5
iter = 50

for i in range(iter):
    with tf.GradientTape() as tape:
        # 训练集
        y_pre_train = tf.nn.softmax(tf.matmul(x_train, w)+b)
        # 交叉熵损失函数
        loss_train = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_train, y_pre_train))
    # 测试集
    y_pre_test = tf.nn.softmax(tf.matmul(x_test, w)+b)
    loss_test = tf.reduce_mean(tf.keras.losses.categorical_crossentropy(y_test, y_pre_test))

    # 准确率
    accuracy_train = tf.reduce_mean(tf.cast(tf.equal(tf.cast(tf.argmax(y_pre_train, axis=1), tf.float32), y_train0), tf.float32))
    accuracy_test = tf.reduce_mean(tf.cast(tf.equal(tf.cast(tf.argmax(y_pre_test, axis=1), tf.float32), y_test0), tf.float32))

    # 梯度下降
    dl_dw, dl_db = tape.gradient(loss_train, [w, b])
    w.assign_sub(learning_rate*dl_dw)
    b.assign_sub(learning_rate*dl_db)

    # 训练过程结果
    print('第%d次 训练集损失函数值为%f, 识别准确率为：%f---测试集损失函数值为%f, 识别准确率为：%f' % (i+1, loss_train, accuracy_train, loss_test, accuracy_test))

print('w的值为', w.numpy())
print('b的值为', b.numpy())
