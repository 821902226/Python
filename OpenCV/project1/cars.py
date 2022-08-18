import cv2
import numpy as np

# 读取视频文件
cap = cv2.VideoCapture('video.mp4')
# 获取去除背景对象
bgsubmog = cv2.createBackgroundSubtractorMOG2()
# 设置矩形最小宽和高
min_w = 60
min_h = 45

while True:
    # 读取一帧
    flag, frame = cap.read()

    if flag:
        # 去除高斯噪声
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame, (3, 3), 5)
        # 去除背景
        mask = bgsubmog.apply(frame)
        # 开运算（去除背景杂点）
        kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        for i in range(3):
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
        # 闭运算（去除车内杂点）
        kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close)
        # 获取轮廓，绘制矩形
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            max_rect = cv2.boundingRect(c)  # 起始点、宽、高
            x, y, w, h = [max_rect[i] for i in range(4)]
            if w > min_w and h > min_h:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('video', frame)

    # 每5毫秒读一帧
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
