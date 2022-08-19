import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('img')
# 读取图片
img = cv2.imread('./chess.png')
# 色彩空间变换
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.SIFT_create()
# 检测关键点
# kp = sift.detect(gray, None)
# 获取关键点和描述子
kp, des = sift.detectAndCompute(gray, None)
# 绘制关键点（image keyPoints outImage）
cv2.drawKeypoints(gray, kp, img)
print(des)

while True:
    # 展示图片
    cv2.imshow('img', img)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
