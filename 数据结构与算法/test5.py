# 选择排序（从无序序列中选出最小值）

def select_sort(alist):
    length = len(alist)
    # 总共要进行n-1次选择
    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    select_sort(alist)
    print(alist)
