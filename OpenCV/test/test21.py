import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('img')
cv2.namedWindow('gray')
cv2.namedWindow('binary')
# 读取图片
img = cv2.imread('./hand.png')
# 色彩空间变换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 图像全局二值化（必须先将图像转化成灰度图，图像、阈值、最大值、类型）
flag, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
# 查找轮廓（图片、轮廓检索模式、轮廓逼近方法）
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓（图片、轮廓、要绘制的轮廓id、轮廓颜色、轮廓粗细）
cv2.drawContours(img, contours, 0, (0, 0, 255), 3)
# 最小外接矩形
min_rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(min_rect)  # 查找旋转矩形的四个顶点
box = np.int32(box)
cv2.drawContours(img, [box], 0, (255, 0, 0), 3)
# 最大外接矩形
max_rect = cv2.boundingRect(contours[0])    # 起始点、宽、高
x, y, w, h = [max_rect[i] for i in range(4)]
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)


while True:
    # 展示图片
    cv2.imshow('img', img)
    cv2.imshow('gray', gray)
    cv2.imshow('binary', binary)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
