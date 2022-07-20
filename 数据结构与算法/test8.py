# 快速排序

def partition(alist, left, right):
    """将数据按照基准值分为两组"""
    base_index = left
    base_data = alist[left]
    # 二者相等时说明分类完成
    while left != right:
        while alist[right] > base_data and left < right:
            right -= 1
        while alist[left] <= base_data and left < right:
            left += 1
        # 确保左边的值小于基准值，右边的值大于基准值
        if left < right:
            alist[left], alist[right] = alist[right], alist[left]
    # 将基准值置于中间
    alist[base_index], alist[left] = alist[left], alist[base_index]
    # 返回基准值的序号
    return left


def quick_sort(alist, left, right):
    # 递归退出条件
    # print('left: %d ---- right: %d' % (left, right))
    if left >= right:
        return
    # 将数据分为两个部分排序
    mid_index = partition(alist, left, right)
    quick_sort(alist, left, mid_index-1)
    quick_sort(alist, mid_index+1, right)


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist)-1)
    print(alist)
