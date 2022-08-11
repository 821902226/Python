import cv2

# 创建窗口
import numpy as np

cv2.namedWindow('dog', cv2.WINDOW_NORMAL)
cv2.namedWindow('dog1', cv2.WINDOW_NORMAL)
cv2.namedWindow('dog2', cv2.WINDOW_NORMAL)
cv2.namedWindow('dog3', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('dog', 600, 480)
cv2.resizeWindow('dog1', 600, 480)
cv2.resizeWindow('dog2', 600, 480)
cv2.resizeWindow('dog3', 600, 480)
# 读取图片
img = cv2.imread('./dog.jpg')
# 制造一张图片(数据类型必须为uint8)
img2 = np.ones((340, 510, 3), 'uint8') * 20
# 图像的加法（亮度增加）
result = cv2.add(img, img2)
# 图像的减法（亮度变暗）
result2 = cv2.subtract(img, img2)
# 图像的融合（alpha，beta分别设置两张图片的权重）
result3 = cv2.addWeighted(img, 0.7, img2, 0.5, 0)

while True:
    # 展示图片
    cv2.imshow('dog', img)
    cv2.imshow('dog1', result)
    cv2.imshow('dog2', result2)
    cv2.imshow('dog3', result3)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
