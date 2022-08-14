import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('sobel_x', cv2.WINDOW_NORMAL)
cv2.namedWindow('sobel_y', cv2.WINDOW_NORMAL)
cv2.namedWindow('sobel_sum', cv2.WINDOW_NORMAL)
cv2.namedWindow('scharr_x', cv2.WINDOW_NORMAL)
cv2.namedWindow('scharr_y', cv2.WINDOW_NORMAL)
cv2.namedWindow('scharr_sum', cv2.WINDOW_NORMAL)
cv2.namedWindow('ldst', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('img', 600, 600)
cv2.resizeWindow('sobel_x', 600, 600)
cv2.resizeWindow('sobel_y', 600, 600)
cv2.resizeWindow('sobel_sum', 600, 600)
cv2.resizeWindow('scharr_x', 600, 600)
cv2.resizeWindow('scharr_y', 600, 600)
cv2.resizeWindow('scharr_sum', 600, 600)
cv2.resizeWindow('ldst', 600, 600)

# 读取图片
img = cv2.imread('./chess.png')
# 索贝尔算子（x方向边缘）--> ksize设置为-1时，即为沙尔算子
sobel_x = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# 索贝尔算子（y方向边缘）
sobel_y = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 索贝尔算子（x,y方向边缘）
sobel_sum = cv2.add(sobel_x, sobel_y)
# 沙尔算子（只能求x或y方向边缘, 不能同时为1，1）
scharr_x = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharr_y = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr_sum = cv2.add(scharr_x, scharr_y)
# 拉普拉斯算子（可以同时求两个方向的边缘，对噪音比较敏感，需要先去噪）
ldst = cv2.Laplacian(img, cv2.CV_64F, ksize=5)


while True:
    # 展示图片
    cv2.imshow('img', img)
    cv2.imshow('sobel_x', sobel_x)
    cv2.imshow('sobel_y', sobel_y)
    cv2.imshow('sobel_sum', sobel_sum)
    cv2.imshow('scharr_x', scharr_x)
    cv2.imshow('scharr_y', scharr_y)
    cv2.imshow('scharr_sum', scharr_sum)
    cv2.imshow('ldst', ldst)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
