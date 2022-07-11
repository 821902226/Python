# tensorflow2.0低阶API基础编程
import tensorflow as tf

# tensorflow2.0版本默认开启eager模式
print(tf.add(2, 4))
print(tf.multiply(2, 4))

num1 = tf.constant(6)
num2 = tf.constant(8)
sum = num1 + num2
# 输出是tensor类型
print(sum)
# 输出numpy类型
print(sum.numpy())

# 创建variable(能够持久化保存)
var = tf.Variable([2, 3, 4])
print(var)

# 创建tensor
zero = tf.zeros([2, 3], tf.float32)
print(zero)
one = tf.ones([2, 3], tf.float32)
print(one)

# tensor形状
print(one.shape)
print(tf.reshape(one, [3, 2]))

# 求平均值
print(tf.math.reduce_mean([[1, 2, 3], [4, 5, 6]], axis=0).numpy())

# 随机生成tensor(服从状态分布)
print(tf.random.normal([2, 3], mean=0, stddev=1).numpy())

# 矩阵的转置
squ = tf.constant([[1, 2, 3], [4, 5, 6]])
print(tf.transpose(squ).numpy())

# 返回一个数组内最大值对应的索引(argmin最小值的索引)
print(tf.math.argmax(squ, axis=1).numpy())
print(tf.math.argmin(squ, axis=0).numpy())

# 将多个tensor进行连接
t1 = tf.constant([[1, 2, 3], [4, 5, 6]])
t2 = tf.constant([[7, 8, 9], [1, 2, 3]])
print(tf.concat([t1, t2], axis=0))

# 数据类型转换
print(t1.dtype)
# t3 = tf.bitcast(t1, 'float32')
t3 = tf.bitcast(t1, tf.float32)
print(t3.dtype)
