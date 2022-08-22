import cv2
import numpy as np

# 读取图片
img1 = cv2.imread('./opencv_search.png')
img2 = cv2.imread('./opencv_orig.png')
# 色彩空间变换
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.SIFT_create()
# 获取关键点和描述子
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
# 创建匹配器
index_params = {'algorithm': 1, 'tree': 5}
search_params = {'checks': 50}
flann = cv2.FlannBasedMatcher(index_params, search_params)
# 对描述子进行匹配计算
matchs = flann.knnMatch(des1, des2, k=2)
# 绘制匹配信息
ret = []
for (m, n) in matchs:
    if m.distance < 0.7 * n.distance:
        ret.append(m)
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matchs, None)

while True:
    # 展示图片
    cv2.imshow('result', img3)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
