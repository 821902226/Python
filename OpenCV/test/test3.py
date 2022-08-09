import cv2


def mouse_callback(event, x, y, flags, userdata):
    """鼠标回调函数"""
    print((event, x, y, flags, userdata))


# 创建视频窗口
cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('mouse', 640, 480)
# 设置鼠标回调函数
cv2.setMouseCallback('mouse', mouse_callback, '鼠标触发')
# 读取图片
img = cv2.imread('test.jpg')

# 显示窗口和背景
while True:
    cv2.imshow('mouse', img)
    # 等待键盘事件
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()


# event的对应事件：
# CV_EVENT_MOUSEMOVE =0,//滑动
# CV_EVENT_LBUTTONDOWN =1,//左键点击
# CV_EVENT_RBUTTONDOWN =2,//右键点击
# CV_EVENT_MBUTTONDOWN =3,//中键点击
# CV_EVENT_LBUTTONUP =4,//左键放开
# CV_EVENT_RBUTTONUP =5,//右键放开
# CV_EVENT_MBUTTONUP =6,//中键放开
# CV_EVENT_LBUTTONDBLCLK =7,//左键双击
# CV_EVENT_RBUTTONDBLCLK =8,//右键双击
# CV_EVENT_MBUTTONDBLCLK =9//中键双击
# flag的对应事件
# CV_EVENT_FLAG_LBUTTON =1,//左键拖拽
# CV_EVENT_FLAG_RBUTTON =2,//右键拖拽
# CV_EVENT_FLAG_MBUTTON =4,//中键拖拽
# CV_EVENT_FLAG_CTRLKEY =8,//按CTRL不放
# CV_EVENT_FLAG_SHIFTKEY =16,//按SHIFT不放
# CV_EVENT_FLAG_ALTKEY =32//按ALT不放
