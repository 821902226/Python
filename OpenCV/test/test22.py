import cv2
import numpy as np

# Harris
# blockSize = 2
# ksize = 3
# k = 0.04

# Shi-tomasi
maxCorners = 1000
qualityLevel = 0.01
minDistance = 10

# 创建窗口
cv2.namedWindow('img')
# 读取图片
img = cv2.imread('./chess.png')
# 色彩空间变换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1.Harris角点检测
# corners = cv2.cornerHarris(gray, blockSize, ksize, k)
# Harris角点标注
# img[corners > 0.01*corners.max()] = [255, 0, 0]

# 2.Shi-tomasi角点检测
corners = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)
corners = np.int32(corners)
# 角点绘制
for corner in corners:
    x = corner[0][0]
    y = corner[0][1]
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

while True:
    # 展示图片
    cv2.imshow('img', img)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
