import cv2

# 创建窗口
cv2.namedWindow('img')
cv2.namedWindow('gray')
cv2.namedWindow('binary')
cv2.namedWindow('adaptive')
# 读取图片
img = cv2.imread('./dog.jpg')
# 色彩空间变换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 图像全局二值化（必须先将图像转化成灰度图，图像、阈值、最大值、类型）
flag, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
# 自适应阈值二值化（灰度图像、最大值、自适应方法、类型、块大小、计算出的平均值减去的常量）
binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 0)


while True:
    # 展示图片
    cv2.imshow('img', img)
    cv2.imshow('gray', gray)
    cv2.imshow('binary', binary)
    cv2.imshow('adaptive', binary_adaptive)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
