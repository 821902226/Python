# 朴素贝叶斯算法对新闻分类
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
# import ssl

# ssl._create_default_https_context = ssl._create_default_https_context

news = fetch_20newsgroups(subset='all')

x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, train_size=0.25)

# 对数据集进行特征抽取
tf = TfidfTransformer()
x_train = tf.fit_transform(x_train)
x_test = tf.transform(x_test)

# 进行朴素贝叶斯算法预测
# alpha设置拉普拉斯平滑系数
mlt = MultinomialNB(alpha=1.0)

mlt.fit(x_train, y_train)

y_predict = mlt.predict(x_test)
print('预测新闻的类别是：', y_predict)

score = mlt.score(x_test, y_test)
print('预测的准确率是：', score)
