import cv2
import numpy as np


def callback(data):
    pass


# 创建窗口
cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('trackbar', 640, 480)
# 创建trackbar    参数：trackbar名字，窗口名字，默认值，最大值，回调函数
cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

# 初始化图像背景
img = np.zeros((640, 480, 3), np.uint8)

while True:
    # 获取当前trackbar的值
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    # 改变背景颜色
    img[:] = [b, g, r]
    # 显示图片
    cv2.imshow('trackbar', img)
    # 等待键盘事件
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
