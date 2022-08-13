import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('img2', cv2.WINDOW_NORMAL)
cv2.namedWindow('img3', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('img', 600, 600)
cv2.resizeWindow('img2', 600, 600)
cv2.resizeWindow('img3', 600, 600)
# 读取图片
img = cv2.imread('./test.jpg')
# 仿射变换之图像平移
M = np.float32([[1, 0, 500], [0, 1, 500]])  # 平移矩阵[[1, 0, x], [0, 1, y]]（左右平移、上下平移，负值表示方向相反）
img2 = cv2.warpAffine(img, M, (2048, 2048))
# 仿射变换之图像旋转(中心点、旋转角度-->默认逆时针、缩放比例)
M = cv2.getRotationMatrix2D((0, 0), -15, 0.5)
img3 = cv2.warpAffine(img, M, (2048, 2048))


while True:
    # 展示图片
    cv2.imshow('img', img)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
