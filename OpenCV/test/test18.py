import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.namedWindow('adaptive', cv2.WINDOW_NORMAL)
cv2.namedWindow('erode', cv2.WINDOW_NORMAL)
cv2.namedWindow('rect', cv2.WINDOW_NORMAL)
cv2.namedWindow('ellipse', cv2.WINDOW_NORMAL)
cv2.namedWindow('cross', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('img', 600, 600)
cv2.resizeWindow('gray', 600, 600)
cv2.resizeWindow('adaptive', 600, 600)
cv2.resizeWindow('erode', 600, 600)
cv2.resizeWindow('rect', 600, 600)
cv2.resizeWindow('ellipse', 600, 600)
cv2.resizeWindow('cross', 600, 600)
# 读取图片
img = cv2.imread('./test.jpg')
# 色彩空间变换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 自适应阈值二值化
binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 0)
# 图像的腐蚀（首先需要构建卷积核，iteration设置图像的腐蚀次数）
kernel = np.ones((3, 3), 'uint8')
erode = cv2.erode(binary_adaptive, kernel, iterations=1)
# 获取形态学卷积核
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
rect = cv2.erode(binary_adaptive, kernel_rect, iterations=1)
ellipse = cv2.erode(binary_adaptive, kernel_ellipse, iterations=1)
cross = cv2.erode(binary_adaptive, kernel_cross, iterations=1)


while True:
    # 展示图片
    cv2.imshow('img', img)
    cv2.imshow('gray', gray)
    cv2.imshow('adaptive', binary_adaptive)
    cv2.imshow('erode', erode)
    cv2.imshow('rect', rect)
    cv2.imshow('ellipse', ellipse)
    cv2.imshow('cross', cross)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
