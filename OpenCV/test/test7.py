import cv2

# 创建窗口
cv2.namedWindow('rmb', cv2.WINDOW_NORMAL)
cv2.namedWindow('rmb2', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('rmb', 800, 480)
cv2.resizeWindow('rmb2', 800, 480)
# 读取图片
img = cv2.imread('./rmb.jpg')
# 通道的分割
b, g, r = cv2.split(img)
# 对通道修改
r[20:100, 20:100] = 0
g[20:100, 20:100] = 0
# 通道的融合(与原图对比)
img2 = cv2.merge((b, g, r))

# 判断摄像头是否打开
while True:
    # 显示图片
    cv2.imshow('rmb', img)
    cv2.imshow('rmb2', img2)
    # 等待键盘事件
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 释放资源
cv2.destroyAllWindows()
