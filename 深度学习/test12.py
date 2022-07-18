# 卷积神经网络实现手写数字识别
import tensorflow as tf

# 获取数据
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 归一化（特征值取值为0～255）
x_train = tf.constant(x_train/255, dtype=tf.float32)
x_test = tf.constant(x_test/255, dtype=tf.float32)

# 建立模型，添加网络层
model = tf.keras.Sequential()
# unit1
model.add(tf.keras.layers.Conv2D(16, kernel_size=(3, 3), padding='same', activation=tf.nn.relu, input_shape=(28, 28, 1)))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
# unit2
model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), padding='same', activation=tf.nn.relu))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
# unit3
model.add(tf.keras.layers.Flatten())
# unit4
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# 设置神经网络模型
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['sparse_categorical_accuracy'])

# 训练神经网络模型
model.fit(x_train, y_train, verbose=1, epochs=5, validation_split=0.2, batch_size=64)

# 评估网络模型
loss, accuracy = model.evaluate(x_test, y_test, verbose=2)
print('损失函数：%f 精确率：%f' % (loss, accuracy))

# 使用模型进行预测
x = tf.reshape(x_test[0], [1, 28, 28])
y_pre = model.predict(x)
print('真实值：', y_test[0])
print('识别值：', tf.math.argmax(y_pre, axis=1).numpy())
