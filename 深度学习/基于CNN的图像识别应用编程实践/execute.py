import tensorflow as tf
import numpy as np
from CnnModel import CnnModel
from getConfig import get_config
import os
import pickle


def read_data(datasets_path, im_dim, channels_num):
    """完成数据读取、格式转换等功能"""
    # 获取文件夹下的所有数据文件名
    files_names = os.listdir(datasets_path)
    # 定义两个空数组来存储特征值和标签值
    images_data = [0 for i in range(len(files_names))]
    images_label = [0 for i in range(len(files_names))]
    # 用于对当前文件进行标记
    index = 0

    # 读取文件数据
    for file_name in files_names:
        print('正在处理数据：', file_name)
        data_dict = unpickle_patch(datasets_path + '/' + file_name)
        images_data[index] = data_dict[b'data']
        images_label[index] = data_dict[b'labels']
        # images_data.shape=(图片数量, 3072),将其转换成图片原本的形状：32*32*3
        images_data[index] = np.reshape(images_data[index], newshape=(len(images_data[index]), im_dim, im_dim, channels_num))
        index += 1
    # 将从多个文件中读取到的数据合并
    images_data = tf.concat(images_data, axis=0)
    images_label = tf.concat(images_label, axis=0)
    return images_data, images_label


def unpickle_patch(file):
    """读取二进制文件，返回读取到的数据"""
    file = open(file, 'rb')
    # 读取文件返回一个字典
    patch_dict = pickle.load(file, encoding='bytes')
    return patch_dict


def train_model(config, array, label):
    # 创建模型
    model = CnnModel(config['learning_rate'], config['drop_rate'], config['classes_num'])
    model = model.create_model()
    # 训练模型
    model.fit(array, label, verbose=1, epochs=5, validation_split=0.2, batch_size=config['batch_size'])
    # 保存模型
    file_name = 'cnn_model.h5'
    save_path = os.path.join('model_saving', file_name)
    model.save(save_path)


def predict(config, data_pre):
    """模型预测"""
    # 加载模型文件
    file_name = 'cnn_model.h5'
    model_path = os.path.join(config['working_directory'], file_name)
    model = tf.keras.models.load_model(model_path)
    # 使用模型进行预测
    label_pre = model.predict(data_pre)
    label_pre = tf.math.argmax(label_pre, axis=1).numpy()
    return label_pre


if __name__ == '__main__':
    # 获取配置文件参数存入字典中
    config_parse = get_config('config.ini')
    # 读取数据
    train_array, train_label = read_data(config_parse['datasets_path'], config_parse['im_dim'], config_parse['channels_num'])
    test_array, test_label = read_data('test_data', config_parse['im_dim'], config_parse['channels_num'])
    # 对输入数据进行归一化处理
    train_array = tf.cast(train_array, dtype='float32')/255
    test_array = tf.cast(test_array, dtype='float32')/255
    # 对标签进行独热编码
    train_label = tf.keras.utils.to_categorical(train_label, 10)
    test_label = tf.keras.utils.to_categorical(test_label, 10)
    # 训练神经网络模型
    train_model(config_parse, train_array, train_label)
    # 加载模型预测结果
    label = predict(config_parse, test_array[:20])
    print('预测结果：', label)
