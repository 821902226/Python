import cv2

# 创建窗口
cv2.namedWindow('img')
cv2.namedWindow('canny')
# 读取图片
img = cv2.imread('./dog.jpg')
# canny边缘检测
canny = cv2.Canny(img, 80, 180)


while True:
    # 展示图片
    cv2.imshow('img', img)
    cv2.imshow('canny', canny)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
