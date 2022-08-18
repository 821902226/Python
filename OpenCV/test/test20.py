import cv2


def drawShape(src, points):
    """绘制多边形和凸包"""
    i = 0
    while i < len(points):
        if i == len(points) - 1:
            x1, y1 = points[i][0]
            x2, y2 = points[0][0]
            cv2.line(src, (x1, y1), (x2, y2), (0, 255, 0), 2)
        else:
            x1, y1 = points[i][0]
            x2, y2 = points[i+1][0]
            cv2.line(src, (x1, y1), (x2, y2), (0, 255, 0), 2)
        i += 1

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
# 计算轮廓面积（单位是像素点）
area = cv2.contourArea(contours[0])
print('轮廓面积是：%d' % area)
# 计算轮廓周长（轮廓、轮廓是否闭合）
length = cv2.arcLength(contours[0], True)
print('轮廓周长是：%d' % length)
# 多边形逼近（轮廓、精度、是否闭合）
approx = cv2.approxPolyDP(contours[0], 3, True)
drawShape(img, approx)
# 凸包
hull = cv2.convexHull(contours[0])
drawShape(img, hull)

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
