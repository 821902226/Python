# 文本特征抽取
from sklearn.feature_extraction.text import CountVectorizer

data = ["life is short, I like python", "life is too long, I do not like python"]

cv = CountVectorizer()

# 提取中文前需要使用jieba分词来对文章进行处理
data = cv.fit_transform(data)   # 得到的data是sparse矩阵类型
data = data.toarray()           # 将sparse矩阵转化为数组矩阵

print(cv.get_feature_names())   # 单个字母不统计
print(data)                     # 数字表示单词的个数
