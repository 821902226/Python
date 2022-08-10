import cv2

# 读取图片
img = cv2.imread('./rmb.jpg')
# 浅拷贝
img1 = img
# 深拷贝
img2 = img.copy()
# 修改img
img[20:50, 20:50] = [0, 255, 255]

# 判断摄像头是否打开
while True:
    # 显示图片
    cv2.imshow('img', img)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    # 等待键盘事件
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 释放资源
cv2.destroyAllWindows()
