# 归并排序

def merge_sort(alist):

    length = len(alist)

    # 序列中只有一个值时不需要再分，形成递归的退出条件
    if length <= 1:
        return alist

    mid = length // 2

    # 获得两个有序的子序列
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    # 将两个有序的子序列合并成一个新的整体
    left_index, right_index = 0, 0
    result = []

    # 对两个有序的序列合并排序(可以另外封装成一个方法)
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            result.append(left_list[left_index])
            left_index += 1
        else:
            result.append(right_list[right_index])
            right_index += 1
    result += left_list[left_index:]
    result += right_list[right_index:]

    # 返回排好序的序列
    return result


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    new_alist = merge_sort(alist)
    print(new_alist)
