import cv2

# 创建视频窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('video', 640, 480)
# 获取视频设备(摄像头)
cap = cv2.VideoCapture(0)
# 从视频文件中读取视频帧(视频文件路径)
# cap = cv2.VideoCapture('aaa.mp4')

# 创建VideoWriter为写多媒体文件
fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
# 设置视频为25帧，分辨率(***get(3),get(4)分别代表原视频流文件的Width和Height***)
vw = cv2.VideoWriter('./out.avi', fourcc, 25, (int(cap.get(3)), int(cap.get(4))))

# 判断摄像头是否打开
while cap.isOpened():
    # 从摄像头读取视频
    flag, frame = cap.read()
    if flag:
        # 将视频帧在窗口显示
        cv2.imshow('video', frame)
        # 将视频帧写多媒体文件
        vw.write(frame)
        # 等待键盘事件
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
vw.release()
cv2.destroyAllWindows()
