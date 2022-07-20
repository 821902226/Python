# 冒泡排序

def bubble_sort(alist):
    length = len(alist)
    # 总共要进行n-1次冒泡
    for i in range(length-1):
        count = 0
        # 每一次冒泡选出剩余数据中的最大值
        for j in range(length-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
        # 当count等于0则表示数据已经完成排序，可以提前结束
        if count == 0:
            break


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(alist)
    print(alist)
