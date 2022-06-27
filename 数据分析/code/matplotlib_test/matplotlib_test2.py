from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

x = range(120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 12), dpi=80)

# x轴样式设置
x_label = ['{}时{}分'.format(int((i / 60) + 8), int(i % 60) + 8) for i in x]

# 设置中文字体，在终端输入fc-list :lang=zh查看系统支持的中文字体， fc-list查看支持的所有字体
my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc', size=16)

# 将坐标轴设置为中文样式显示 rotation表示字体旋转角度
plt.xticks(x[::5], x_label[::5], rotation=60, fontproperties=my_font)
plt.yticks(y, fontproperties=my_font)

# 添加描述信息
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度', fontproperties=my_font)
plt.title('某地温度变化表', fontproperties=my_font)

plt.plot(x, y)
plt.savefig('code/matplotlib_test/test2.jpg')
plt.show()
