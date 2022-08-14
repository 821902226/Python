import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('dog', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('box', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('blur', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('gaussian', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('median', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('lateral', cv2.WINDOW_AUTOSIZE)
# 读取图片
img = cv2.imread('./dog.jpg')
# 方盒滤波(normalize==True时就是均值滤波)
box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# 均值滤波(平滑处理)
blur = cv2.blur(img, (5, 5))
# 高斯滤波(高斯噪声)
gaussian = cv2.GaussianBlur(img, (5, 5), sigmaX=1)
# 中值滤波(椒盐噪声)
median = cv2.medianBlur(img, 3)
# 双边滤波(美颜：保留边缘，对边缘内部进行平滑处理)
lateral = cv2.bilateralFilter(img, 5, 20, 50)


while True:
    # 展示图片
    cv2.imshow('dog', img)
    cv2.imshow('box', box)
    cv2.imshow('blur', blur)
    cv2.imshow('gaussian', gaussian)
    cv2.imshow('median', median)
    cv2.imshow('lateral', lateral)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
