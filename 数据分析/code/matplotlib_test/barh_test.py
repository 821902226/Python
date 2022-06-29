from matplotlib import pyplot as plt
from matplotlib import font_manager

x = list(range(1, 4))
x_label = ['斗罗大陆', '斗破苍穹', '完美世界']
y = [11756, 12357, 30923]

plt.figure(figsize=(8, 6), dpi=100)

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc')

plt.yticks(x, x_label, fontproperties=my_font)

plt.xlabel('电影票房', fontproperties=my_font)
plt.ylabel('电影', fontproperties=my_font)
plt.title('电影对应的票房', fontproperties=my_font)

# 绘制横的条形图 height用于指定条形的宽度
plt.barh(x, y,  color='cyan', height=0.5)

plt.savefig('code/matplotlib_test/barh_test.jpg')

plt.show()
