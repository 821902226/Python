from matplotlib import pyplot as plt

x = range(0, 24, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 设置图片大小
plt.figure(figsize=(12, 8), dpi=50)

# 绘图
plt.plot(x, y)

# 设置xy轴坐标值
plt.xticks(range(24))
plt.yticks(range(min(y), max(y)+1))

# 保存图片
plt.savefig('code/matplotlib_test/test1.jpg')

# 展示图形
plt.show()
