# tf-idf文本特征抽取(用于评估一个词对于文章分类的重要程度)
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

sentence1 = '今天很残酷，明天更残酷，后天很美好，但绝大部分是死在昨天晚上的，所以每个人都不要放弃今天'
sentence2 = '我们看到的从很远星系来的光是在几百万年前发出的，这样当我们看宇宙时，我们是在看它的过去'
sentence3 = '如果只以一种方式了解某种事物，你就不会真正了解它，了解事物真正含义的秘密在于如何将其与我们所了解的事物联系起来'

# 分词处理(先转化为列表，然后转化为字符串)
sentence1 = list(jieba.cut(sentence1))
sentence2 = list(jieba.cut(sentence2))
sentence3 = list(jieba.cut(sentence3))
# 使用空格将每个词连接
s1 = " ".join(sentence1)
s2 = " ".join(sentence2)
s3 = " ".join(sentence3)

tf = TfidfVectorizer()

# 提取中文前需要使用jieba分词来对文章进行处理
data = tf.fit_transform([s1, s2, s3])   # 得到的data是sparse矩阵类型
data = data.toarray()           # 将sparse矩阵转化为数组矩阵

print(tf.get_feature_names())   # 单个字母不统计
print(data)                     # 数字表示单词的个数
