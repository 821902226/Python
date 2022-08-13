import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('new', cv2.WINDOW_NORMAL)
cv2.namedWindow('not', cv2.WINDOW_NORMAL)
cv2.namedWindow('and', cv2.WINDOW_NORMAL)
cv2.namedWindow('or', cv2.WINDOW_NORMAL)
cv2.namedWindow('xor', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('new', 600, 600)
cv2.resizeWindow('not', 600, 600)
cv2.resizeWindow('and', 600, 600)
cv2.resizeWindow('or', 600, 600)
cv2.resizeWindow('xor', 600, 600)
# 读取图片
img = cv2.imread('./test.jpg')
print(img.shape)
test = np.zeros((2048, 2048, 3), np.uint8)
test[500:1500, 500:1500, :] = 255
# 对图片进行非运算（黑变白、白变黑）
img1 = cv2.bitwise_not(img)
# 对图片进行与运算（同时为白时，结果才是白）
img2 = cv2.bitwise_and(img, test)
# 对图片进行或运算(有白则为白)
img3 = cv2.bitwise_or(img, test)
# 对图片进行异或运算(一白一黑则为白)
img4 = cv2.bitwise_xor(img, test)


while True:
    # 展示图片
    cv2.imshow('new', img)
    cv2.imshow('not', img1)
    cv2.imshow('and', img2)
    cv2.imshow('or', img3)
    cv2.imshow('xor', img4)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
