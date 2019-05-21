# find a position
def partition(array, left, right):

    i = left-1
    for j in range(left, right):
        if array[j] <= array[right]:
            i += 1
            # swap array[j] & array[i] 交换第一个比尾巴大的数和其后第一个比尾巴小的数
            if i < j:
                array[j], array[i] = array[i], array[j]
                print(array)
    # 交换最后一个数和他应该在位置的数，i+1是最后一个元素该呆的位置
    array[i+1], array[right] = array[right], array[i+1]
    return i+1


def quick_sort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quick_sort(array, left, pivot-1)
        quick_sort(array, pivot+1, right)


array = [3, 2, 11, 0, 9, 8, 7, 6, 1, 4]
quick_sort(array, 0, 9)
print(array)