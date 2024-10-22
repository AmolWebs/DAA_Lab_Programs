import threading

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def threaded_merge_sort(arr, left, right, depth):
    if left < right:
        mid = (left + right) // 2
        if depth <= 0:
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
        else:
            left_thread = threading.Thread(target=threaded_merge_sort, args=(arr, left, mid, depth - 1))
            right_thread = threading.Thread(target=threaded_merge_sort, args=(arr, mid + 1, right, depth - 1))
            left_thread.start()
            right_thread.start()
            left_thread.join()
            right_thread.join()

        merge(arr, left, mid, right)

if __name__ == "__main__":
    print("\nName : Amol Subhash Dangat\nRoll No : 09\n")
    arr1 = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr1)
    merge_sort(arr1, 0, len(arr1) - 1)
    print("Sorted array (regular merge sort):", arr1)
    arr2 = [12, 11, 13, 5, 6, 7]
    max_depth = 3
    threaded_merge_sort(arr2, 0, len(arr2) - 1, max_depth)
    print("Sorted array (multithreaded merge sort):", arr2)