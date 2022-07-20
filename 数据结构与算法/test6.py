# 插入排序算法

def insert_sort(alist):
    length = len(alist)
    for i in range(1, length):
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)
