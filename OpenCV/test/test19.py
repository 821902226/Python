import cv2

# 创建窗口
cv2.namedWindow('img')
cv2.namedWindow('img1')
cv2.namedWindow('img2')
cv2.namedWindow('gray')
cv2.namedWindow('binary')
cv2.namedWindow('open')
cv2.namedWindow('close')
cv2.namedWindow('grad')
cv2.namedWindow('tophat')
cv2.namedWindow('blackhat')
# 读取图片
img = cv2.imread('./dog.jpg')
img1 = cv2.imread('./dotin.png')
img2 = cv2.imread('./tophat.png')
# 色彩空间变换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 图像全局二值化（必须先将图像转化成灰度图，图像、阈值、最大值、类型）
flag, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
# 图像开运算（先腐蚀再膨胀，消除图形外部的噪点）
kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
morph_open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_open)
# 图像闭运算（先膨胀再腐蚀，消除图形内部的噪点）
kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
morph_close = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel_close)
# 形态学梯度（原图减去腐蚀后的图）--> 可以用来求边缘
kernel_grad = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
morph_grad = cv2.morphologyEx(morph_close, cv2.MORPH_GRADIENT, kernel_grad)
# 顶帽运算（原图减去开运算后的图）--> 保留大图形外部的点
kernel_tophat = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 19))
morph_tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel_tophat)
# 黑帽运算（原图减去闭运算后的图）--> 保留大图形内部的点
kernel_blackhat = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
morph_blackhat = cv2.morphologyEx(img1, cv2.MORPH_BLACKHAT, kernel_blackhat)


while True:
    # 展示图片
    cv2.imshow('img', img)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('gray', gray)
    cv2.imshow('binary', binary)
    cv2.imshow('open', morph_open)
    cv2.imshow('close', morph_close)
    cv2.imshow('grad', morph_grad)
    cv2.imshow('tophat', morph_tophat)
    cv2.imshow('blackhat', morph_blackhat)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
