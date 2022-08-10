import cv2


def callback(data):
    pass


# 创建窗口
cv2.namedWindow('color', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('color', 800, 480)
# 读取图片
img = cv2.imread('./rmb.jpg')
# 常见色彩空间
colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL, cv2.COLOR_BGR2YUV]
# 添加trackbar用以改变色彩空间
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces)-1, callback)

while True:
    # 获取trackbar的值
    index = cv2.getTrackbarPos('curcolor', 'color')
    # 改变图片色彩空间
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    # 展示图片
    cv2.imshow('color', cvt_img)
    # 设置退出
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
