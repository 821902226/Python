import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('dog', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('dog2', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('dog3', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('dog4', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('dog5', cv2.WINDOW_AUTOSIZE)
# 读取图片
img = cv2.imread('./dog.jpg')
# 图片的缩放(图片源、指定图片大小， 缩放算法)
img2 = cv2.resize(img, (255, 170), interpolation=cv2.INTER_AREA)
# 图片的按比例缩放(图片源、指定图片比例， 缩放算法)
img3 = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
# 图片翻转（flipCode=0时上下翻转，大于0时左右翻转，小于0时上下左右翻转）
img4 = cv2.flip(img, -1)
# 图片旋转ROTATE_90_CLOCKWISE-->顺时针90° ROTATE_180-->顺时针180° ROTATE_90_COUNTERCLOCKWISE-->逆时针90°
img5 = cv2.rotate(img, rotateCode=cv2.ROTATE_90_CLOCKWISE)

while True:
    # 展示图片
    cv2.imshow('dog', img)
    cv2.imshow('dog2', img2)
    cv2.imshow('dog3', img3)
    cv2.imshow('dog4', img4)
    cv2.imshow('dog5', img5)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
