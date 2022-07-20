# 希尔排序算法

def shell_sort(alist):
    length = len(alist)
    # 分组间隔
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j = i
            # 插入排序
            while j > gap-1:
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(alist)
    print(alist)
