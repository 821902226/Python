import cv2

# 创建窗口(AUTOSIZE表示自适应无法调整，NORMAL可以调整窗口大小)
cv2.namedWindow('new', cv2.WINDOW_NORMAL)
# 读取图片
img = cv2.imread('test.jpg')
# 调整窗口大小
cv2.resizeWindow('new', 520, 500)
# 显示窗口
cv2.imshow('new', img)

# 设置窗口显示时间（毫秒） ---- 0表示一直显示
key = chr(cv2.waitKey(0))    # 得到的结果时ASCII码的数字表示，使用chr()方法将其转化成ASCII码
if key == 'q':
    # 按下q时，关闭窗口释放资源
    cv2.destroyAllWindows()
elif key == 's':
    # 按下s时，保存图片
    cv2.imwrite('save.png', img)
