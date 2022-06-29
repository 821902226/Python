from matplotlib import pyplot as plt
from matplotlib import font_manager

x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

plt.figure(figsize=(10, 6), dpi=100)

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc')

x_label = ['{}岁'.format(i) for i in x]

plt.xticks(x, x_label, fontproperties=my_font)

plt.xlabel('岁数', fontproperties=my_font)
plt.ylabel('个数', fontproperties=my_font)
plt.title('每年的女朋友数量', fontproperties=my_font)

# 绘制散点图
plt.scatter(x, y,  color='cyan', linewidth=3)

plt.savefig('code/matplotlib_test/scatter.jpg')

plt.show()
