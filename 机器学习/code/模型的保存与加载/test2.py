# K-近邻算法训练模型的加载
import joblib
import numpy as np

# 加载Knn训练模型
knn_model = joblib.load('./机器学习/code/模型的保存与加载/knn_model.pkl')

# 使用模型预测结果
y_predict = knn_model.predict(np.array([1.11, 1.58, 99, 18, 6]).reshape(1, 5))

print('预测结果：', y_predict)
