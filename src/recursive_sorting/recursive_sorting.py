# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i = i+1
        else:
            merged_arr[k] = arrB[j]
            j = j+1
        k = k+1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i = i+1
        k = k+1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j = j+1
        k = k+1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:

        left = merge_sort(arr[0: int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])

        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
