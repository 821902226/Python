import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('dog', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('dog1', cv2.WINDOW_AUTOSIZE)
# 读取图片
img = cv2.imread('./dog.jpg')
# 卷积核
kernel = np.ones((3, 3), 'float32') / 10
# 图像的卷积
dst = cv2.filter2D(img, -1, kernel)


while True:
    # 展示图片
    cv2.imshow('dog', img)
    cv2.imshow('dog1', dst)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
