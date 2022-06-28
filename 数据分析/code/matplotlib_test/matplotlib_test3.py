from matplotlib import pyplot as plt
from matplotlib import font_manager

x = range(11, 31)
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

plt.figure(figsize=(10, 6), dpi=100)

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc')

x_label = ['{}岁'.format(i) for i in x]

plt.xticks(x, x_label, fontproperties=my_font)

plt.xlabel('岁数', fontproperties=my_font)
plt.ylabel('个数', fontproperties=my_font)
plt.title('每年的女朋友数量', fontproperties=my_font)

# 绘制网格 alpha设置网格的透明度(从0到1)
plt.grid(alpha=0.3)

# 可以使用linestyle设置线条风格 linewidth设置线条粗细
plt.plot(x, y1, label='自己', color='cyan', linestyle='--', linewidth=5)
plt.plot(x, y2, label='同桌', color='gold', linestyle='-', linewidth=5)

# 添加图例
plt.legend(prop=my_font)

plt.savefig('code/matplotlib_test/test3.jpg')

plt.show()
