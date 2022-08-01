# 卷积神经网络模型类
import tensorflow as tf


class CnnModel(object):
    """卷积神经网络模型类"""
    def __init__(self, learning_rate, drop_rate, classes_num):
        # 学习率
        self.learning_rate = learning_rate
        # Dropout神经元失效的概率
        self.drop_rate = drop_rate
        # 识别图片的种类
        self.classes_num = classes_num

    def create_model(self):
        # 建立模型
        model = tf.keras.Sequential()
        # 卷积层和池化层完成特征提取
        # 添加二维卷积层32*32*3
        model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
        # 添加二维最大池化层
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
        # 添加批量池化层
        model.add(tf.keras.layers.BatchNormalization())
        # 添加第二个卷积层
        model.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), padding='same', activation='relu'))
        # 添加第二个二维池化层
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
        # 添加批量池化层
        model.add(tf.keras.layers.BatchNormalization())
        # 添加第三个卷积层
        model.add(tf.keras.layers.Conv2D(128, kernel_size=(3, 3), padding='same', activation='relu'))
        # 添加第三个二维池化层
        model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
        # 添加批量池化层
        model.add(tf.keras.layers.BatchNormalization())

        # 添加Flatten层，将数据压成一个维度，减少参数的数量
        model.add(tf.keras.layers.Flatten())
        # 添加Dropout层防止过拟合
        model.add(tf.keras.layers.Dropout(self.drop_rate))
        # 添加全连接层，分类问题使用softmax函数(10分类)
        model.add(tf.keras.layers.Dense(self.classes_num, activation='softmax'))

        # 卷积神经网络模型的编译
        model.compile(loss=tf.losses.categorical_crossentropy, optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate), metrics=['accuracy'])

        return model
