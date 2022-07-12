# tensorflow2.0高阶API(tf.keras)
import tensorflow as tf
import numpy as np

# 1.构建神经网络模型
model = tf.keras.Sequential()
# 添加一层全连接神经网络
model.add(tf.keras.layers.Dense(input_dim=1, units=1))
# 对神经网络模型进行编译
model.compile(loss='mse', optimizer='sgd')

# 2.训练神经网络模型
x = np.linspace(-10, 10, 500)
y = 2 * x + 100 + tf.random.normal([500, 1], 0, 1)
# 开始训练
model.fit(x, y, verbose=1, epochs=200, validation_split=0.2)

# 3.保存神经网络模型
filename = './深度学习/line_model.h5'
model.save(filename)
print('保存的神经网络模型为： line_model.h5')

# 4.加载模型进行预测
x = tf.constant([0.5])
model = tf.keras.models.load_model(filename)
y = model.predict(x)
print('预测结果为： ', y)
