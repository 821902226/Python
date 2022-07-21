# 二分法查找

def binary_search_01(alist, data):
    """递归方式实现"""
    length = len(alist)
    # 递归退出条件
    if length == 0:
        return False
    # 找到中间点
    mid = length // 2
    if alist[mid] == data:
        return True
    elif alist[mid] > data:
        return binary_search_01(alist[:mid], data)
    elif alist[mid] < data:
        return binary_search_01(alist[mid+1:], data)


def binary_search_02(alist, data):
    """循环方式实现"""
    length = len(alist)
    left = 0
    right = length-1
    while left <= right:
        mid = (left + right) // 2
        if alist[mid] == data:
            return True
        elif alist[mid] > data:
            right = mid - 1
        elif alist[mid] < data:
            left = mid + 1
    return False


if __name__ == "__main__":
    alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # 查找的序列必须为有序序列
    flag1 = binary_search_01(alist, 32)
    flag2 = binary_search_02(alist, 77)
    print(flag1)
    print(flag2)
