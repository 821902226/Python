import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('draw', cv2.WINDOW_NORMAL)
cv2.resizeWindow('draw', 640, 480)
# 创建背景
img = np.zeros((480, 640, 3))
# 画直线（设置直线的两个端点和颜色，还可以设置线宽和线型）
cv2.line(img, (0, 0), (640, 480), (255, 0, 0))
# 画矩形(矩形的两个对角、颜色、线宽、线型)
cv2.rectangle(img, (0, 0), (640, 480), (255, 0, 0), 5)
# 画圆(原点、半径、颜色、线宽-->-1表示填充)
cv2.circle(img, (320, 240), 50, (0, 0, 255), -1)
# 画椭圆(中心、长和宽、旋转角度、开始角度、结束角度、颜色)
cv2.ellipse(img, (320, 240), (100, 50), 0, 0, 360, (0, 255, 0))
# 画多边形（多边形的端点、是否封闭、颜色）
pos = np.array([(320, 10), (170, 100), (470, 100)], 'int32')
cv2.polylines(img, [pos], True, (0, 255, 0))
# 填充多边形
cv2.fillPoly(img, [pos], (0, 120, 50))
# 绘制文本(字符串、左下角坐标、字体、字号、颜色)
cv2.putText(img, 'Hello, world', (10, 450), 3, 1, (0, 255, 0))

# 判断摄像头是否打开
while True:
    # 显示图片
    cv2.imshow('draw', img)
    # 等待键盘事件
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 释放资源
cv2.destroyAllWindows()
