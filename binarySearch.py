import bisect


def binary_tree(arr, target, start=None, end=None):
    mid = (end + start) // 2
    if arr[mid] < target:
        print(mid)
        return binary_tree(arr, target, mid + 1, end)
    elif arr[mid] > target:
        print(mid)
        return binary_tree(arr, target, start, mid)
    elif start > end:
        return -1
    else:
        return mid


my_list = [x for x in range(1, 10)]
n = 9
print(my_list[binary_tree(my_list, n, 0, len(my_list) - 1)])
print()
print(my_list.index(bisect.bisect(my_list, n))) # 이진탐색 함수
